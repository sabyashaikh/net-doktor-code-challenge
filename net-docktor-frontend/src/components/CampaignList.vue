<template>
  <div>
      <div class="header">
        <span class="title">Alle Kampagnen</span>
        <base-button @click="showCampaignModal">KAMPAGNE ERSTELLEN</base-button>
      </div>
      <div class="table">
        <div class="table__filter">
          <span class="table__filter__text">Status filtern:</span>
          <base-multiselect :options="statusOptions"
                            class="table__filter__multiselect"
                            @select="handleStatusSelected"
          ></base-multiselect>
        </div>
        <progress-indicator v-if="loading"></progress-indicator>
        <base-table v-else
                    :headers="headers"
                    :items="items"
        ></base-table>
      </div>
  </div>
</template>

<script>
import BaseButton from "./BaseComponents/BaseButton.vue"
import BaseMultiselect from "./BaseComponents/BaseMultiselect.vue";
import BaseTable from "@/components/BaseComponents/BaseTable.vue";
import ProgressIndicator from "@/components/BaseComponents/ProgressIndicator.vue";
import axios from 'axios'

export default {
    components: {
      BaseTable, BaseButton, BaseMultiselect, ProgressIndicator
    },
    data() {
      return {
        axios,
        statusOptions: ['Created', 'Booked', 'Archived'], //Can be accessed via API from backend
        selectedStatus:[],
        headers:["CS-ID","Kunde","Kampagnenname", "Start", "Ende", "Status"],
        items:[],
        loading: true
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
        url="http://localhost:8081/campaigns"
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
  display: flex;
  justify-content: space-between;
}

.table{
  height: 751px;
  margin: 16px 0 0;
  border: solid 1px #d8d8d8;
}

.table__filter{
  height: 70px;
  padding: 12px 16px 12px 753px;
  background-color: #f4f6f8;
  border: solid 1px #d8d8d8;
  display: flex;
  justify-content: end;

}
.table__filter__text{
  margin-block: auto;
  font-size: 14px;
  letter-spacing: 0.5px;
  color: #7c7c7c;
}


.table__filter__multiselect {
  width: 40%;
  padding-left: 1em;
}
</style>