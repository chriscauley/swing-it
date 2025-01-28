<template>
  <div>
    <unrest-schema-form form_name="schema/bar" />
  </div>
</template>

<script>

export default {
  methods: {
    deleteItem(item) {
      this.$ui.alert()
      this.$ui.confirm()
      this.$ui.addToast("Hello")
      this.$ui.toast.warning("Hello")
    }
  }
}
</script>