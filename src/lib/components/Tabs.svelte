<script lang="ts">
    import Tab, { Icon, Label } from '@smui/tab';
    import TabBar from '@smui/tab-bar';
    
  
    let tabs = [
      {
        icon: 'access_time',
        label: 'Home',
        route: '/'
      },
      {
        icon: 'near_me',
        label: 'Nearby',
        route: '/near'
      },
      {
        icon: 'favorite',
        label: 'About',
        route: '/about'
      },
    ];
    let active = tabs[0];

    function handleTabClick() {
      navigate(`${active.route}`);
    }

  </script>
  <!-- 
  <nav>
    <TabBar {tabs} let:tab bind:active>
      <Tab {tab} on:click={() => handleTabClick()}>
        <Icon class="material-icons">{tab.icon}</Icon>
        <Label>{tab.label}</Label>
      </Tab>
    </TabBar>
  </nav>
  -->

  <nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/settings">Settings</a>
  </nav>
  
  <slot></slot>
 