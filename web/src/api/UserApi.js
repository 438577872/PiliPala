import requests from "@/utils/request";


export function findAllVideoByPage(ID) {
    return requests({
        url: 'user/findAllVideoByPage/' + ID,
        method: 'get',
    })
}


export function login(data) {
    return requests({
        url: 'user/login',
        method: 'post',
        data
    })
}


export function register(data) {
    return requests({
        url: 'user/register',
        method: 'post',
        data
    })
}


export function logout(token) {
    return requests({
        url: 'user/logout',
        method: 'post',
        data: {token}
    })
}

export function getInfo(token) {
    return requests({
        url: 'user/getInfo',
        method: 'post',
        data: {token}
    })
}





