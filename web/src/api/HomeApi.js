import requests from "@/utils/request";


export function homeInit() {
    return requests({
        url: '/home/' ,
        method: 'get',
    })
}




