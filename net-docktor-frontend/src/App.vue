<script setup>
import CampaignList from "./components/CampaignList.vue";
</script>


<template>
  <div class="mainContainer">
    <div class="header">
      <img src="../src/assets/img/menu.svg"
           class="menu"
      >
      <span class="Kampagnenmanager">
        Kampagnenmanager
      </span>
    </div>
    <!-- router-view can be used here to display component dynamically -->
    <div class="content">
      <campaign-list></campaign-list>
    </div>
  </div>
</template>


<style scoped>
.mainContainer {
  width: 100%;
  height: 100vh;
  padding: 0 0 32px;
  background-color: #fafafa;
}

.Kampagnenmanager {
  width: 252px;
  height: 29px;
  margin: 0 0 0 16px;
  font-size: 24px;
  font-weight: bold;
  font-stretch: normal;
  font-style: normal;
  line-height: normal;
  letter-spacing: 0.86px;
  color: #fff;
}

.header {
  display: flex;
  width: 100%;
  height: 64px;
  margin: 0 0 40px;
  padding: 18px 1084px 17px 64px;
  box-shadow: 0 0 4px 0 rgba(0, 0, 0, 0.12), 0 4px 4px 0 rgba(0, 0, 0, 0.24);
  background-color: #00bef7;
}

img.menu {
  width: 24px;
  height: 24px;
  object-fit: contain;
}


.content {
  margin: 4em;
  padding: 2em;
  border-radius: 2px;
  box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.24), 0 0 2px 0 rgba(0, 0, 0, 0.12);
  background-color: #fff;
}
</style>
