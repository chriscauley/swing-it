<template>
  <div v-if="lookup && limbs">
    <div class="bar-detail">
      <div
        v-for="count, index in bar.counts"
        :key="index"
        :class="css.count(count, index)"
        >
        <div v-for="limb in makeLimbs(count)" :key="limb">
          <div
            :class="limb.cls"
            @click="removeLimb(limb)"
            >{{ limb.note?.short || '..' }}</div>
        </div>
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

const newBar = () => ({
  counts: range(8).map(() => [])
})

export default {
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
        const limb = limbs.find(limb => console.log(note.limb, limb) ||limb.slug === note.limb)
        limb.cls = 'btn -primary'
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
    }
  }
}
</script>