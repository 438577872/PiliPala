import router from './router'
import store from './store'
import {getToken} from '@/utils/auth' // get token from cookie


// NProgress.configure({showSpinner: false}) // NProgress Configuration

// const whiteList = ['/login'] // no redirect whitelist

router.beforeEach(async (to, from, next) => {
    const hasToken = getToken()
    let name = store.getters.name
    if (name) {
        next()
    } else {
        try {
            await store.dispatch("user/getInfo")
            next()
        } catch (e) {
        }

    }

    if (hasToken) {
        if (to.path === '/login' || to.path === '/register') {
            next({path: '/'})
        }

        next()
    } else {
        if (to.path.split('/')[1] === 'space') {
            next('/')
        } else {
            next()
        }
        await store.dispatch('user/getInfo')

    }
    next()
})

router.afterEach(() => {
})
