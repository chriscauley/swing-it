<template>
  <div v-if="lookup && limbs">
    <div class="bar-detail">
      <div
        v-for="count, index in bar.counts"
        :key="index"
        :class="css.count(count, index)"
        >
        <pose-button
          v-for="limb in makeLimbs(count, index)"
          :key="limb"
          :limb="limb"
          @click="removeLimb(limb, count)"
        />
        <button class="btn -success bar-detail__select-count" @click="current_count=index">
          <i class="fa fa-check" />
        </button>
      </div>
    </div>
    <div class="bar-editor__pose-box">
       <div v-for="poses, limb in lookup.by_limb" :key="limb" class="bar-editor__pose-limb">
        <div
          class="btn -primary"
          v-for="pose in poses"
          :key="pose.id"
          @click="clickPose(pose)"
        >
          {{ pose.short }}
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { range } from 'lodash'

import PoseButton from './PoseButton.vue'

const newBar = () => ({
  counts: range(8).map(() => [])
})

export default {
  components: { PoseButton },
  data() {
    const css = {
      count: (count, index) => [
        "bar-detail__count",
        this.current_count === index && '-current',
      ],
    }

    return {
      bar: newBar(),
      current_count: 0,
      hovering: null,
      css,
    }
  },
  computed: {
    lookup() {
      return this.$store.pose.getLookup()
    },
    limbs() {
      return this.$store.pose.getLimbs()
    }
  },
  methods: {
    makeLimbs(count) {
      const limbs = this.limbs.ALL.map(limb => ({
        ...limb,
        cls: 'btn -text -empty'
      }))
      count.map((id) => {
        const note = {...this.lookup.by_id[id]}
        const limb = limbs.find(limb => limb.slug === note.limb)
        limb.note = note
      })
      return limbs
    },
    clickPose(pose) {
      const count = this.bar.counts[this.current_count]
      if (count.includes(pose.id)) {
        count.splice(count.indexOf(pose.id), 1)
      } else {
        const existing = count.find(
          id => this.lookup.by_id[id].limb === pose.limb
        )
        if (existing) {
          count.splice(count.indexOf(existing), 1)
        }
        count.push(pose.id)
      }
    },
    removeLimb(limb, count) {
      count.splice(count.indexOf(limb.note.id), 1)
    }
  }
}
</script>