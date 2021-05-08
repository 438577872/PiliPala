import axios from 'axios'
import Message from "element-ui/packages/message/src/main";
import {getToken} from "@/utils/auth";
// import { getToken } from '@/utils/auth'
let service = axios.create({
    baseURL: '/api/',

})

service.interceptors.request.use(
    config => {
        config.headers['token'] = getToken()
        return config
    }
)

service.interceptors.response.use(
    response => {
        const res = response.data
        if (res.msg) {
            Message(res.msg)
        }
        // if the custom code is not 20000, it is judged as an error.
        if (res.code !== 20000 && res.code !== 20001) {
            return Promise.reject(new Error(res.msg || 'Error'))
        } else {
            return res
        }
    },
    error => {
        return Promise.reject(error)
    }
)

export default service
