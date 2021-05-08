import {login, logout, getInfo} from '@/api/UserApi'
import {getToken, setToken, removeToken, setUserId} from '@/utils/auth'
// import * as router from "vue-router";
// import router from 'vue-router'
// import {adminRoutes, asyncRoutes, resetRouter, userRoutes} from '@/router'
// import Vue from 'vue'
import router from '@/router'

const getDefaultState = () => {
    return {
        token: getToken(),
        name: '',
        avatar: ''
    }
}

const state = getDefaultState()

const mutations = {
    RESET_STATE: (state) => {
        Object.assign(state, getDefaultState())
    },
    SET_TOKEN: (state, token) => {
        state.token = token
    },
    SET_NAME: (state, name) => {
        state.name = name
    },
    SET_AVATAR: (state, avatar) => {
        state.avatar = avatar
    },
    SET_UP_ID: (state, up_id) => {
        state.up_id = up_id
    },
}

const actions = {
    // user login
    login({commit, state}, userInfo) {
        return new Promise((resolve, reject) => {
            login(userInfo).then(response => {
                const {data} = response
                commit('SET_TOKEN', data.token)

                setToken(data.token)
                // console.log(getToken())
                // setUserId(data.id)
                router.push('/')
                resolve()
            }).catch(error => {
                reject(error)
            })
        })
    },

    // get user info
    getInfo({commit, state}) {
        return new Promise((resolve, reject) => {
            getInfo().then(response => {
                const {data} = response
                if (!data) {
                    return reject('Verification failed, please Login again.')
                }
                const {name, avatar, id} = data
                commit('SET_NAME', name)
                commit('SET_AVATAR', avatar)
                commit('SET_UP_ID', id)
                // router.push('/')
                // router.
                resolve(data)
            }).catch(error => {
                reject(error)
            })
        })
    },

    // user logout
    logout({commit, state}) {
        return new Promise((resolve, reject) => {
            logout(state.token).then(() => {
                removeToken() // must remove  token  first
                commit('RESET_STATE')
                router.push('/')
                resolve()
            }).catch(error => {
                reject(error)
            })
        })
    },

    // remove token
    resetToken({commit}) {
        return new Promise(resolve => {
            removeToken() // must remove  token  first
            commit('RESET_STATE')
            resolve()
        })
    }
}

export default {
    namespaced: true,
    state,
    mutations,
    actions
}

