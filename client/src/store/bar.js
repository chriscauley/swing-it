import { RestStorage } from '@unrest/vue-storage'

export default () => {
  const storage = RestStorage('schema/pose', { collection_slug: 'schema/pose' })
  return storage
}
