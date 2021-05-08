import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Big from "../views/account/Big";
import Layout from "../views/account/Layout";
import AccountHome from "../views/space/AccountHome";
import SpaceLayout from "../views/space/SpaceLayout";
import SpaceHome from "../views/space/SpaceHome";
import SpaceSettings from "../views/space/SpaceSettings";
import SpaceDynamic from "../views/space/SpaceDynamic";
import SpaceVideo from "../views/space/SpaceVideo";
import SpaceChannel from "../views/space/SpaceChannel";
import SpaceFavouriteList from "../views/space/SpaceFavouriteList";
import SpaceSubs from "../views/space/SpaceSubs";
import SpaceContributeLayout from "../views/space/SpaceContributeLayout";
import SpaceAudio from "../views/space/SpaceAudio";
import SpaceArticle from "../views/space/SpaceArticle";
import SpaceAlbum from "../views/space/SpaceAlbum";
import SpaceUpload from "@/views/space/SpaceUpload";
import VideoPlay from "@/views/video/VideoPlay";
import AccountLogin from "@/views/account/AccountLogin";
import AccountRegister from "@/views/account/AccountRegister";
import NotFound from "@/views/errPage/NotFound";
import Test from "@/views/Test";

Vue.use(VueRouter)


const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
    return originalPush.call(this, location).catch(err => err)
}

export const SpaceContributeList = [
    {
        path: 'video',
        name: '视频',
        component: SpaceVideo,
    },
    {
        path: 'audio',
        name: '音频',
        component: SpaceAudio,
    },

    {
        path: 'article',
        name: '专栏',
        component: SpaceArticle,
    },
    {
        path: 'album',
        name: '相册',
        component: SpaceAlbum,
    },
    {
        path: 'upload',
        name: '投稿',
        component: SpaceUpload,

    }
]
export const spaceList = [
    {
        path: 'home',
        name: '主页',
        component: SpaceHome,

    },
    {
        path: 'dynamic',
        name: '动态',
        component: SpaceDynamic,
    },
    {
        path: '',
        name: '投稿',
        component: SpaceContributeLayout,
        children: [
            ...SpaceContributeList]
        ,
        meta: {
            url: 'video'
        }
    },
    {
        path: 'channel',
        name: '频道',
        component: SpaceChannel,
    },
    {
        path: 'favouriteList',
        name: '收藏',
        component: SpaceFavouriteList,
    },
    {
        path: 'subs',
        name: '订阅',
        component: SpaceSubs,
    },
    {
        path: 'settings',
        name: '设置',
        component: SpaceSettings,
    },
    // {
    //     path: '*',
    //     name: '404',
    //     component: NotFound,
    // },
]


const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path:'/1',
        name:'Test',
        component:Test
    }
    ,
    {
        path: '/login',
        name: 'login',
        component: AccountLogin
    },
    {
        path: '/register',
        name: 'register',
        component: AccountRegister
    },
    {
        path: '/account',
        name: 'account',
        component: Layout,
        children: [
            {
                path: 'home',
                name: 'account/home',
                component: AccountHome,

            },
            {
                path: 'big',
                name: 'big',
                component: Big,

            },

        ]
    },
    {
        path: '/space/:id/',
        name: 'space',
        component: SpaceLayout,
        children: [
            {
                path: '',
                redirect: 'home'
            },
            ...spaceList
        ]
    },
    {
        path: '/video',
        name: 'VideoPlay',
        component: VideoPlay
    },
    // {
    //     path: '*',
    //     name: '404',
    //     component: NotFound
    // }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})


export default router
