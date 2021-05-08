const getters = {
    token: state => state.user.token,
    avatar: state => state.user.avatar,
    name: state => state.user.name,
    up_id:state => state.user.up_id,
}
export default getters
