<script lang="ts">
  import { T, useFrame } from '@threlte/core'
  import { interactivity, Grid, OrbitControls, Text } from '@threlte/extras'
  import { spring } from 'svelte/motion'
  import Link from './Link.svelte';
  import Plan from './Plan.svelte';
  import Nuage from './Nuage.svelte';
  import User from './User.svelte'
  import Lan from './Lan.svelte'
  import { onMount } from 'svelte';
  import type { Links, Flows, Lans, Users } from '$lib/type'
  import { Color, LoadingManager, Vector3 } from 'three';
  import Flow from './Flow.svelte';
  import {css4Colors} from '$lib/couleurs'

  
	let links: Links = []
  let flows: Flows = []
  let lans: Lans = []
  let users: Users = []

  // Charger le fichier JSON au chargement du composant
  onMount(async () => {
    try {
      const response1 = await fetch('data.json');
      const data = await response1.json();
      flows = data.Flows;
      links = data.Links;
      lans = data.Lans;
      users = data.Users;

      console.log("Chargement réussi!")

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

<T.PerspectiveCamera makeDefault position={[10, 150, 300]} fov={100}>
	<OrbitControls enableDamping />
</T.PerspectiveCamera>

<T.DirectionalLight position={[0, 10, 10]} castShadow />

<Plan plan={-1} color={css4Colors.midnightblue} name="Transport"/>  <!--Bleu foncé-->
<Plan plan={0}  color={css4Colors.darkblue} name="Routage"/>    <!--Bleu-vert moyen-->
<Plan plan={1}  color={css4Colors.darkcyan} name="Usagers"/>    <!--Bleu-vert-->
<Plan plan={2}  color={css4Colors.aqua} name="Services"/>   <!--Bleu vert très clair-->


{#if lans}
  {#each lans as item, i}
    {#if item?.type=='DC'}
    <Nuage 
      centre={item.position}
      name={item.name}
      type="DC"
      color={item.color}></Nuage>
    {:else}
    <Lan
    position={item.position}
    name={item.name}
    color={item.color}></Lan>
    {/if}
  {/each}
{/if}

{#if users}
  {#each users as item, i}
    {#if item}
      <User position={item.position}/>
    {/if}
  {/each}
{/if}


{#if flows}
  {#each flows as item, i}
    {#if item}
      <Flow controlPoints={item.controlPoint} color={item.color}/>
    {/if}
  {/each}
{/if}


<Text
  text="Les réseaux, c'est beau!"
  position={[-20,200,0]}
  fontSize={6}/>


{#if links}
  {#each links as item, i}
  {#if item}
    <Link source={item.source} destination={item.destination} color={item.color}/>
  {/if}
  {/each}
{/if}


