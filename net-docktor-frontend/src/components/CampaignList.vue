<template>
  <div>
      <div class="header flex-container">
        <span class="title">Alle Kampagnen</span>
        <base-button @click="showCampaignModal=true">KAMPAGNE ERSTELLEN</base-button>
      </div>
      <div class="table">
        <div class="table__filter flex-container">
          <span class="table__filter__text">Status filtern:</span>
          <base-select :options="statusOptions"
                       class="table__filter__multiselect"
                       @close="handleStatusSelected"
          ></base-select>
        </div>
        <div class="table__content">
          <progress-indicator v-if="loading"></progress-indicator>
          <base-table v-else
                    :headers="headers"
                    :items="items"
                    class="margin-top"
        ></base-table>
        </div>
      </div>
      <div v-if="showCampaignModal">
        <base-modal title="Kampagne erstellen">
          <campaign-creation @created="getCampaigns" @close="showCampaignModal=false"></campaign-creation>
        </base-modal>
      </div>
  </div>
</template>

<script>
import BaseButton from "./BaseComponents/BaseButton.vue"
import BaseSelect from "./BaseComponents/BaseSelect.vue";
import BaseTable from "@/components/BaseComponents/BaseTable.vue";
import ProgressIndicator from "@/components/BaseComponents/ProgressIndicator.vue";
import axios from 'axios'
import BaseModal from "@/components/BaseComponents/BaseModal.vue";
import CampaignCreation from "@/components/CampaignCreation.vue";

export default {
    components: {
      BaseModal,
      CampaignCreation,
      BaseTable, BaseButton, ProgressIndicator, BaseSelect
    },
    data() {
      return {
        axios,
        statusOptions: ['Created', 'Booked', 'Archived'], //Can be accessed via API from backend
        selectedStatus:[],
        headers:["CS-ID","Kunde","Kampagnenname", "Start", "Ende", "Status"],
        items:[],
        loading: true,
        showCampaignModal: false,
      }
    },
  mounted() {
      this.getCampaigns()
  },
  methods:{
    handleStatusSelected(values){
      /**
       * A request to backend is sent to retrieved entries for the selected status
       * */
      this.getCampaigns(values)
    },
    getCampaigns(status=null){
      /**
       * A request to backend is sent to retrieve campaigns
       * If status is not passed all campaigns are retrieved else the campaigns are filter based on status values
       * */
      this.loading=true
      let url = "http://localhost:8081/campaigns/"
      if(status){
        url=`http://localhost:8081/campaigns/?status=${status}`
      }
      this.axios.get(url,
          {headers: {
        'Content-Type': 'application/json'
        }}).then((response)=>{
          this.items=response.data
      }).catch((error)=>{
        console.debug(error)
      }).finally(()=>{
        this.loading=false
      })
    }
  }
}

</script>



<style scoped>

.title{
  font-size: 24px;
  font-weight: bold;
  color: #444;
}

.header{
  height: 40px;
  justify-content: space-between;
}

.table{
  height: 751px;
  margin: 16px 0 0;
  border: solid 1px #d8d8d8;
}

.table__filter{
  height: 70px;
  width: 100%;
  padding: 1em;
  background-color: #f4f6f8;
  border: solid 1px #d8d8d8;
  justify-content: end;
}

.table__filter__text{
  margin-block: auto;
  font-size: 14px;
  letter-spacing: 0.5px;
  color: #7c7c7c;
  padding-right: 1em;
}


.table__filter__multiselect {
  width: 400px;
  min-width: 400px;
}

.table__content{
  height: calc(100% - 70px);
  width: 100%;
  overflow: auto;
}

@media (max-width: 768px) {
  .table__filter {
    padding: 0.25em;
  }
}

</style>