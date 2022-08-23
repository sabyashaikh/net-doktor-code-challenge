<template>
  <div>
    <progress-indicator v-if="saving"></progress-indicator>
    <div v-else>
      <div class="row">
        <div class="label col-md-3">
          Kampagnenname*:
        </div>
        <div class="col-md-9">
          <input v-model="campaign.name" class="form-input w-100"/>
          <div v-if="nameError" class="error">Dieses Feld kann nicht leer sein</div>
        </div>
      </div>
      <div class="row">
        <div class="label col-md-3">
          Kunde*:
        </div>
        <div class="col-md-9">
          <input v-model="campaign.customer" class="form-input w-100"/>
          <div v-if="customerError" class="error">Dieses Feld kann nicht leer sein</div>
        </div>
      </div>
      <div class="row">
        <div class="label col-md-3">
          Laufzeit:
        </div>
        <div class="flex-container col-md-9">
          <div class="start mr-3">
            <span class="mr-2 subtext">Start*:</span>
            <input v-model="campaign.start" type="date" class="form-input"/>
          </div>
          <div class="end">
            <span class="mr-2">End*:</span>
            <input v-model="campaign.end" type="date" class="form-input"/>
          </div>
          <div v-if="startError || endError" class="my-auto error">Dieses Feld kann nicht leer sein</div>
        </div>
      </div>
      <div class="row">
        <div class="label col-md-3">
          Status:
        </div>
        <div class="col-md-9">
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
        <div class="label col-md-3">
          Notiz:
        </div>
        <div class="col-md-9">
          <textarea
              v-model="campaign.note"
              rows="4"
              class="form-input w-100">
          </textarea>
        </div>
      </div>
      <div class="row footer flex-container">
        <base-button
            class="footer-btn"
            btn-type="secondary"
            @btn-click="cancel">
          ABBRECHEN
        </base-button>
        <base-button
            class="footer-btn"
            @btn-click="saveCampaign">
          ERSTELLEN
        </base-button>
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

.footer{
  justify-content: end;
}

.subtext {
  font-size: 14px;
  letter-spacing: 0.5px;
  color: #444;
}

.error {
  font-size: 10px;
  color: #f66363;
  margin-left: 2px;
}

.footer-btn{
  margin-left: 0.5rem;
}

.form-input {
  border-radius: 2px;
  border: solid 1px #d8d8d8;
}

@media (max-width: 768px) {

  .start, .end {
    width: 100%;
    margin-top: 2px;
    margin-right: 0 !important;
  }

  .footer-btn{
    margin-top: 2px;
    margin-left: 0 !important;
    width: 100%;
  }

  .label{
    text-align: left;
  }

  input{
    width: 100%;
  }

  .error{
    margin-left: 0;
  }
}

textarea:focus, input:focus{
    outline: none;
    box-shadow: 0 0 0 3px rgba(0, 183, 249, 0.2);
}
</style>