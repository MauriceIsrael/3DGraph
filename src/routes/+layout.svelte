<script lang="ts">
    import TopAppBar, {
      Row,
      Section,
      Title,
      AutoAdjust,
    } from '@smui/top-app-bar';
    import IconButton, { Icon } from '@smui/icon-button';
    import LinearProgress from '@smui/linear-progress';
  
    let topAppBar: TopAppBar;
  </script>

<LinearProgress indeterminate />
<TopAppBar bind:this={topAppBar} variant="standard" dense>
    <nav> 
        <Row>
            <Section>
                <a href="/">
                  <IconButton class="material-icons">diversity_2</IconButton>
                </a>
            </Section>
                
            <Section align="end" toolbar>
                <a href="/about">
                    <IconButton class="material-icons">question_mark</IconButton>
                </a>
            </Section>
       </Row>
      </nav>
</TopAppBar>
<AutoAdjust {topAppBar}>
  <slot />
</AutoAdjust>

<style>
    /* Hide everything above this component. */
    :global(#smui-app),
    :global(body),
    :global(html) {
      display: block !important;
      height: auto !important;
      width: auto !important;
      position: static !important;
    }
  </style>