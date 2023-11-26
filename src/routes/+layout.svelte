<script lang="ts">
  import Tab, { Icon, Label } from '@smui/tab';
  import TabBar from '@smui/tab-bar';
  
  let tabs = [
    {
      icon: 'home',
      label: 'Home',
      route: '/',
    },
    {
      icon: 'code',
      label: 'Code', 
      route: '/code'
    },
    {
      icon: 'link',
      label: 'Inexorable', 
      route: '/inexorable'
    },
    {
      label: 'About',
      route: '/about'
    }
  ];
  let active = tabs[0];
  let closed = false;

</script>

<!-- <LinearProgress indeterminate {progress} {closed} /> -->

<TabBar {tabs} let:tab bind:active>
  <nav> 
    <Tab {tab} href={tab.route}>
      {#if tab.icon != ''}
      <Icon class="material-icons">{tab.icon}</Icon>  
      {/if}
      <Label>{tab.label}</Label>
    </Tab>
  </nav>
</TabBar>

<slot />