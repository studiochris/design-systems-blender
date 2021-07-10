<template>
  <div class="ui-tab-container">
    <ui-tab-bar :tabs="tabs"></ui-tab-bar>
    <section class="ui-tabs-content">
      <template :slot-scope="{selectedIndex}">No Tabs Defined</template>
    </section>
  </div>
</template>

<script>
import UiTabBar from "./UiTabBar.vue";
export default {
  components: { UiTabBar },
  name: "UiTabContainer",
  data() {
    return {
      tabs: [],
      selectedIndex: 1
    };
  },
  mounted() {
    const vm = this;

    console.log(`created`);
    console.log(vm.$children, vm.$children.length);
    this.$nextTick(() => {
      vm.tabs = vm.$children.filter(tab => tab.data?.isUiTab);
    })
  },
};
</script>

<style lang="scss">
</style>