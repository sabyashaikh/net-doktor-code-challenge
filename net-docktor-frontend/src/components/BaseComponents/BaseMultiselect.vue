<template>
  <div>
    <Multiselect
      v-model="value"
      :options="options"
      :searchable="true"
      mode="tags"
      class="multiselect-blue"
      @select="$emit('select', (Object.values(value)))"
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
      options: {
        required: true,
        type: Array
      }
    },
    data() {
      return {
        value: null,
      }
    }
  }
</script>

<style src="@vueform/multiselect/themes/default.css">

.multiselect-blue {
  --ms-tag-bg: #2563EB !important;
  --ms-tag-color: #DBEAFE !important;
}
</style>