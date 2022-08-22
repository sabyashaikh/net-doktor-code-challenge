<script setup>
import PrimaryButton from "./BaseComponents/BaseButton.vue"

</script>

<template>
  <div>
      <div class="header">
        <span class="title">Alle Kampagnen</span>
        <primary-button @click="showCampaignModal">KAMPAGNE ERSTELLEN</primary-button>
      </div>
      <div class="table">
        <div class="table__filter">
          <span class="table__filter__text">Status filtern:</span>
          <input>
        </div>
        <div class="table__header"></div>
      </div>
  </div>
</template>


<style scoped>


</style>