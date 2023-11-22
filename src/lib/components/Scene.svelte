<script lang="ts">
  import { T, useFrame } from '@threlte/core'
  import { interactivity, Grid, OrbitControls, Text } from '@threlte/extras'
  import { spring } from 'svelte/motion'
  import Link from './Link.svelte';
  import Plan from './Plan.svelte';
  import { onMount } from 'svelte';
  import type { Links } from '$lib/type'
  
	let links: Links = []

  // Charger le fichier JSON au chargement du composant
  onMount(async () => {
    try {
      const response = await fetch('jeu_de_donnees_100_lignes.json');
      const data = await response.json();
      links = data.Links;
    } catch (error) {
      console.error('Erreur lors du chargement du fichier JSON :', error);
    }
  });


  interactivity()
  const scale = spring(1)
  let rotation = 0
  useFrame((state, delta) => {
    rotation += delta
  })

</script>


<Grid
	infiniteGrid
	sectionColor="#4a4b4a"
	sectionSize={20}
	cellSize={20}
	fadeDistance={400}
/>

<T.PerspectiveCamera makeDefault position={[10, 100, 100]} fov={60}>
	<OrbitControls enableDamping />
</T.PerspectiveCamera>

<T.DirectionalLight position={[0, 10, 10]} castShadow />



<Plan plan={-1} color="darkblue"/>
<Plan plan={0}/>

<Text
  text="Salut les gars!"
  position={[10,60,10]}
  fontSize={1.8}/>

<div>
  {#if links}
	  {#each links as item, i}
    <Link source={item.source} destination={item.destination} color={item.color}/>
	  {/each}
  {/if}
</div>

