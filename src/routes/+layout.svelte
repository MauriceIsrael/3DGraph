<script lang="ts">
  import Tab, { Icon, Label } from '@smui/tab';
  import TabBar from '@smui/tab-bar';
  import LinearProgress from '@smui/linear-progress';

  let tabs = [
    {
      icon: 'home',
      label: 'Home',
      route: '/',
    },
    {
      label: 'About',
      route: '/about'
    }
  ];
  let active = tabs[0];

</script>

<LinearProgress indeterminate />
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