<template>
  <div :class="['button', btnType]" @click.stop="$emit('btn-click')">
    <span class="button-text">
      <slot></slot>
    </span>
  </div>
</template>

<script>
export default {
    props: {
      btnType: {
        required: false,
        type: String,
        default: "primary"
      }
    }
  }
</script>


<style scoped>

.button {
  width: 209px;
  height: 36px;
  border-radius: 2px;
  box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.24), 0 0 2px 0 rgba(0, 0, 0, 0.12);
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}

.primary{
  background-color: #00bef7;
  color: #ffffff;
}

.secondary{
  background-color:  #ffffff;
  color: #00bef7;
}

.primary.button:hover{
  background-color: #00b7f9
}

.secondary.button:hover{
  color: #00b7f9
}

.button-text{
  font-size: 14px;
  font-weight: bold;
  text-align: center;
  letter-spacing: 0.5px;
}


</style>