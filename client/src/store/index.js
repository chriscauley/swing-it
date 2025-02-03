import bar from './bar'
import pose from './pose'

const store = {}

const modules = {
  bar,
  pose,
}

export default {
  install(app) {
    app.config.globalProperties.$store = store
    store._app = app

    Object.entries(modules).forEach(([name, module]) => {
      this[name] = store[name] = module({ store })
    })
  }
}
