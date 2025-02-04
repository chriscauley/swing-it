import { capitalize } from 'lodash'
import { RestStorage } from '@unrest/vue-storage'

const replaces = [
  ['Right ', 'R-'],
  ['Left ', 'L-'],
  ['Hammer', 'H'],
  ['moulinet', 'Moul'],
  ['Audience', 'Crowd'],
  ['up', '⇧'],
  ['down', '⇩'],
  ['Backpack', 'Back'],
]

export default () => {
  const storage = RestStorage('schema/pose', { collection_slug: 'schema/pose' })
  storage.api.fetch('limb').then((r) => {
    const limbs = (storage.api.state.limbs = { ALL: [] })
    r.data.forEach((slug) => {
      limbs[slug] = {
        slug,
        name: capitalize(slug),
      }
      limbs.ALL.push(limbs[slug])
    })
  })
  storage.getLookup = () => {
    const { items = [] } = storage.getPage({ query: { per_page: 1e8 } }) || {}
    const by_limb = {}
    const by_id = {}
    const by_slug = {}
    items.forEach(({ ...i }) => {
      i.short = i.name
      replaces.forEach(([a, b]) => {
        i.short = i.short.replace(a, b)
      })
      by_limb[i.limb] = by_limb[i.limb] || []
      by_limb[i.limb].push(i)
      by_id[i.id] = i
      by_slug[i.slug] = i
    })
    return { by_limb, by_id, by_slug }
  }
  storage.getLimbs = () => storage.api.state.limbs
  return storage
}
