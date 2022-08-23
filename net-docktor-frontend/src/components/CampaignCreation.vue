<template>
  <div>
    <progress-indicator v-if="saving"></progress-indicator>
    <div v-else>
      <div class="row">
        <div class="label col-3">
          Kampagnenname*:
        </div>
        <div class="col-9">
          <input v-model="campaign.name" class="form-input w-100"/>
          <div v-if="nameError" class="error">Dieses Feld kann nicht leer sein</div>
        </div>
      </div>
      <div class="row">
        <div class="label col-3">
          Kunde*:
        </div>
        <div class="col-9">
          <input v-model="campaign.customer" class="form-input w-100"/>
          <div v-if="customerError" class="error">Dieses Feld kann nicht leer sein</div>
        </div>
      </div>
      <div class="row">
        <div class="label col-3">
          Laufzeit:
        </div>
        <div class="d-flex col-9">
          <div class="me-3">
            <span class="ml-2 subtext">Start*:</span>
            <input v-model="campaign.start" type="date" class="form-input"/>
          </div>
          <div>
            <span class="ml-2">End*:</span>
            <input v-model="campaign.end" type="date" class="form-input"/>
          </div>
          <div v-if="startError || endError" class="ml-2 my-auto error">Dieses Feld kann nicht leer sein</div>
        </div>
      </div>
      <div class="row">
        <div class="label col-3">
          Status:
        </div>
        <div class="col-9">
          <base-select
              :value="campaign.status"
              :options="['Created','Booked', 'Archived']"
              :can-deselect="false"
              mode="single"
              @select="(value)=>campaign.status=value"
          >
          </base-select>
        </div>
      </div>
      <div class="row">
        <div class="label col-3">
          Notiz:
        </div>
        <div class="col-9">
          <textarea v-model="campaign.note" rows="4" class="form-input w-100"></textarea>
        </div>
      </div>
      <div class="row d-flex justify-content-end">
        <base-button btn-type="secondary" @btn-click="cancel">ABBRECHEN</base-button>
        <base-button class="ml-2" @btn-click="saveCampaign">ERSTELLEN</base-button>
      </div>
    </div>
  </div>
</template>

<script>
import BaseSelect from "@/components/BaseComponents/BaseSelect.vue";
import BaseButton from "@/components/BaseComponents/BaseButton.vue";
import ProgressIndicator from "@/components/BaseComponents/ProgressIndicator.vue";
import axios from 'axios'

export default {
  components: {
    BaseSelect, BaseButton, ProgressIndicator
  },
  data() {
    return {
      axios,
      campaign: {
        name: "",
        customer: "",
        start: "2022-08-01",
        end: "2022-08-01",
        note: "",
        status: "Created"
      },
      saving: false,
      nameError: false,
      customerError: false,
      startError: false,
      endError: false,
      statusError: false
    }
  },
  methods: {
    saveCampaign() {
      /**
       * A request to backend is sent to save campaign
       * */
      if(!this.validate()) return //Checks for correct validation of the data before sending it to backend
      this.saving = true
      this.axios.post("http://localhost:8081/campaigns/", {...this.campaign},
          {
            headers: {
              'Content-Type': 'application/json'
            }
          }).then((response) => {
        this.items = response.data
        this.$emit("created")
        this.$emit('close')
      }).catch((error) => {
        console.debug(error)
      }).finally(() => {
        this.saving = false
      })
    },
    cancel() {
      this.$emit('close')
    },
    validate(){
      /**
       * Checks for correct validation of the data
       */
      this.nameError = this.campaign.name===""
      this.customerError = this.campaign.customer===""
      this.customerError = this.campaign.customer===""
      this.startError = this.campaign.start===""
      this.endError = this.campaign.end===""
      return !this.nameError && !this.customerError && !this.endError && !this.startError
    },
  },
}
</script>

<style scoped>
.row {
  padding: 1em;
}

/* Clear floats after the columns */
.row:after {
  content: "";
  display: table;
  clear: both;
}

.label {
  padding-right: 2em;
  font-size: 16px;
  font-weight: bold;
  letter-spacing: 0.57px;
  color: #444;
  text-align: right;
}

input {
  height: 36px;
}

.subtext {
  font-size: 14px;
  letter-spacing: 0.5px;
  color: #444;
}

.error {
  font-size: 10px;
  color: #f66363;
}

.form-input {
  border-radius: 2px;
  border: solid 1px #d8d8d8;
}

@media (max-width: 768px) {
  [class*="col-"] {
    width: 100% !important;
  }
}

textarea:focus, input:focus{
    outline: none;
    box-shadow: 0 0 0 3px rgba(0, 183, 249, 0.2);
}
</style>