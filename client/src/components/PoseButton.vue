<template>
  <div :class="cls" @mouseover="hovering = true" @mouseout="hovering = false">
    {{ limb.note?.short || '..' }}
  </div>
</template>

<script>
export default {
  props: {
    limb: Object,
  },
  data() {
    return {
      hovering: false,
    }
  },
  computed: {
    cls() {
      if (!this.limb.note) {
        return 'btn -empty -text'
      }
      return this.hovering ? 'btn -danger' : 'btn -primary'
    },
  },
}
</script>
