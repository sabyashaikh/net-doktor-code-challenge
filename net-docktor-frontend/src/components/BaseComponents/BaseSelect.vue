<template>
  <div>
    <Multiselect
      v-model="selectedValue"
      :options="options"
      :searchable="true"
      :mode="mode"
      :can-deselect="canDeselect"
      @select="$emit('close',selectedValue)"
      @deselect="$emit('close',selectedValue)"
      @clear="$emit('close',[])"
    >
      <template v-if="mode==='tags'"
                v-slot:clear="{ clear }"
      >
        <span class="count">
          {{ selectedValue.length }}
        </span>
        <span class="multiselect-clear" @click="clear">
          <span class="multiselect-clear-icon"></span>
        </span>
      </template>
    </Multiselect>
  </div>
</template>

<script>
  import Multiselect from '@vueform/multiselect'

  export default {
    components: {
      Multiselect,
    },
    props: {
      value:{
        required: false,
        default: null,
        type: [String, Array]
      },
      options: {
        required: true,
        type: Array
      },
      mode: {
        required: false,
        type: String,
        default: "tags"
      },
      canDeselect:{
        required: false,
        type: Boolean,
        default: true
      }
    },
    data() {
      return {
        selectedValue: null,
      }
    },
    mounted() {
      this.selectedValue = this.value
    }
  }
</script>

<style scoped>
.count{
  width: 24px;
  height: 24px;
  margin-right: 4px;
  padding: 0 7px 0 8px;
  border-radius: 2px;
  background-color: #00bef7;
  color: #fff;
  font-size: 14px;
}
</style>

<style src="@vueform/multiselect/themes/default.css">

</style>