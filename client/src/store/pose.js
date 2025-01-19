import { RestStorage } from '@unrest/vue-storage'

export default () => {
  const storage = RestStorage('pose', { collection_slug: 'pose' })
  return storage
}

