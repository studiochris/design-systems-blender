<template>
  <ul class="ui-tab-bar">
    <li v-for="(tab, index) in computedTabs" :key="index">
      <ui-tab-button :tab="tab">{{ tab.name }}</ui-tab-button>
    </li>
  </ul>
</template>

<script>
import UiTabButton from "./UiTabButton";

export default {
  name: "UiTabBar",
  components: {
    UiTabButton
  },
  props: {
    tabs: {
      type: Array,
      required: true
    },
    selectedIndex: {
      type: Number,
      default: 1
    }
  },
  computed: {
    computedTabs() {
      return this.tabs.filter(tab => tab.isUiTab)
    },
    selectedTab() {
      return this.tabs[selectedIndex];
    }
  },
  created(){
    console.log(this.tabs);
  }
};
</script>

<style lang="scss">
</style>