<template>
  <div>
    <el-popover
            placement="bottom"
            width="300"
            trigger="hover"
            v-if="avatar">
      <AccountLogoutDialog></AccountLogoutDialog>
      <div slot="reference">

        <router-link :to="'/space/' + up_id +'/home' ">
          <el-avatar :src="staticAvatar + avatar">

          </el-avatar>
        </router-link>
      </div>
      <!--      </router-link>-->
    </el-popover>

    <el-popover
            v-else
            placement="bottom"
            width="300"
            trigger="hover">
      <!--      <AccountLoginDialog/>-->
      <AccountLoginDialog></AccountLoginDialog>
      <div slot="reference">
        <router-link to="/login">
          <el-avatar >
            登录
          </el-avatar>
        </router-link>
      </div>
    </el-popover>
  </div>
</template>

<script>
    import AccountLogoutDialog from "@/views/account/AccountLogoutDialog";
    import AccountLoginDialog from "@/views/account/AccountLoginDialog";
    import {staticAvatar} from "@/config";
    import {mapGetters} from "vuex";

    export default {
        name: "PublicAvatar",
        computed: {
            ...mapGetters([
                'avatar','up_id'
            ])
        },
        components: {AccountLoginDialog, AccountLogoutDialog},
        data() {
            return {
                staticAvatar
            }
        },
        methods: {
            // to()
        }

    }
</script>

<style scoped>

</style>