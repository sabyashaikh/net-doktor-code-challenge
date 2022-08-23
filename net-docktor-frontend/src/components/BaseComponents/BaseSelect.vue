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
    >
      <template v-slot:multipleLabel="{ values }">
          <div class="multiselect-multiple-label">
            {{ values.length }} characters selected
          </div>
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

<style src="@vueform/multiselect/themes/default.css">

</style>