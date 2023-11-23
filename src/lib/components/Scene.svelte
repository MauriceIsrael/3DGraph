<script lang="ts">
  import { T, useFrame } from '@threlte/core'
  import { interactivity, Grid, OrbitControls, Text } from '@threlte/extras'
  import { spring } from 'svelte/motion'
  import Link from './Link.svelte';
  import Plan from './Plan.svelte';
  import Nuage from './Nuage.svelte';
  import User from './User.svelte'
  import { onMount } from 'svelte';
  import type { Links, Flows } from '$lib/type'
  import { Color, LoadingManager, Vector3 } from 'three';
  import Flow from './Flow.svelte';
  
  
  
	let links: Links = []
  let flows: Flows = []

  // Charger le fichier JSON au chargement du composant
  onMount(async () => {
    try {
      const response1 = await fetch('jeu_de_donnees\ WAN.json');
      const data = await response1.json();
      flows = data.Flows;
      links = data.Links;
      console.log(JSON.stringify(flows))
     
      let d = new Vector3(10,12,10)
      console.log(JSON.stringify(d))

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

<T.PerspectiveCamera makeDefault position={[10, 100, 100]} fov={60}>
	<OrbitControls enableDamping />
</T.PerspectiveCamera>

<T.DirectionalLight position={[0, 10, 10]} castShadow />

<Plan plan={-1} color="Aqua" name="Transport"/>  <!--Bleu foncé-->
<Plan plan={0}  color="Turquoise" name="Routage"/>    <!--Bleu-vert moyen-->
<Plan plan={1}  color="cadetblue"name="Usagers"/>    <!--Bleu-vert-->
<Plan plan={2}  color="turquoise3 "name="Services"/>   <!--Bleu vert très clair-->

<Nuage 
  centre={new Vector3(-24, 40, -76)}
  name="DC1"
  type="DC"
  color="yellow"></Nuage>

  <Nuage 
  centre={new Vector3(85, 40, -26)}
  name="DC2"
  type="DC"
  color="red"></Nuage>

  <Nuage 
  centre={new Vector3(52, 40, 48)}
  name="DC3"
  type="DC"
  color="blue"></Nuage>

<User position={new Vector3(-56,80,96)}/>
<!--
<Flow controlPoints={[new Vector3(50.823639748672186,  80, -72.77495475906467), 
                     new Vector3(46.708360090888476, 40, -8.987295221367836),
                     new Vector3(56.56546341334605, 0, -26.383951081811134),
                     new Vector3(53.18195108142242,-40, 17.54081181625277),
                     new Vector3(53.18195108142242,-40, 17.54081181625277),
                     new Vector3(76.56604844745885, 0, 8.16334644256776),
                     new Vector3(-35.66069209032165,-40, -36.459772896155975),
                      new Vector3(-48.490911352329704, -40,-53.22247191009173),
                      new Vector3(49.548440226699356, 0, 77.41350380337241),
                      new Vector3(46.708360090888476, 40, -8.987295221367836),
                      new Vector3(-50.823639748672186,80,-72.77495475906467)
         
                     
                     ]}/>-->

<div>
  {#if flows}
	  {#each flows as item, i}
      {#if item}
        <Flow controlPoints={item.controlPoint}/>
      {/if}
	  {/each}
  {/if}
</div>

<Text
  text="Les réseaux, c'est beau!"
  position={[-20,100,0]}
  fontSize={6}/>

<div>
  {#if links}
	  {#each links as item, i}
    <Link source={item.source} destination={item.destination} color={item.color}/>
	  {/each}
  {/if}
</div>

