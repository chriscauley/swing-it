<template>
  <div>
    <bar-editor :bar="selected_bar" />
  </div>
</template>

<script>
export default {
  data() {
    return {
      selected_bar: null,
      current_index: 0,
    }
  },
  computed: {
    bars() {
      return []
    },
  },
}
</script>
