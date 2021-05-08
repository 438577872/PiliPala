import requests from "@/utils/request";


export function getVideoUrlBySeriesIdAndNo(params) {
    return requests({
        url:'video/getVideoUrlBySeriesIdAndNo',
        method:'get',
        params
    })
}
export function sendBarrage(data) {
    return requests({
        url:'video/sendBarrage',
        method:'post',
        data
    })
}
export function fetchBarrageBySeriesId(params) {
    return requests({
        url:'video/fetchBarrageBySeriesId',
        method:'get',
        params
    })
}

export function fetchComment(params) {
    return requests({
        url:'video/fetchComments',
        method:'get',
        params
    })
}



export function fetchVideoNos(params) {
    return requests({
        url:'video/fetchVideoNos',
        method:'get',
        params
    })
}



