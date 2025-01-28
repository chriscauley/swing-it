<template>
  <router-view />
  <unrest-ui />
</template>

<script>
export default {
  computed: {
    pose() {
      return this.$store.pose.getPage({ query: { per_page: 5000 } })
    }
  }
}
</script>