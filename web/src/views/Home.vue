<template>
  <div style="width: 100%">
    <PublicHeader></PublicHeader>
    <HomeBody></HomeBody>
  </div>
</template>

<script>
    import HomeBody from "@/views/home/HomeBody";
    import PublicHeader from "./Public/PublicHeader";

    export default {
        name: 'Home',
        components: {
            PublicHeader,
            HomeBody,
        }
    }
</script>
