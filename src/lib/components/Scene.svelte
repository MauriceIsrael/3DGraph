<script>
  import { T, useFrame } from '@threlte/core'
  import { interactivity, Grid, OrbitControls } from '@threlte/extras'
  import { spring } from 'svelte/motion'
  import { Color, LineCurve3, Vector3 } from 'three'
  import Link from './Link.svelte';
    import Plan from './Plan.svelte';

  interactivity()
  const scale = spring(1)
  let rotation = 0
  useFrame((state, delta) => {
    rotation += delta
  })

  // create a smooth curve from 4 points
  const curve2 = new LineCurve3(new Vector3(-8, 20, 3), new Vector3(12, 20, 10))
  // convert curve to an array of 100 points
  let points2 = curve2.getPoints(100)

  const link1 = {
    source: new Vector3(-8,0,6),
    destination: new Vector3(-12,0,-4),
    color: "blue"
  };
  

  const link2 = {
    source: new Vector3(28,20,-16),
    destination: new Vector3(28,-20,-16),
    color: "green"
  };

  const link3 = {
    source: new Vector3(-8,20,3),
    destination: new Vector3(12,20,10),
    color: "yellow"
  };
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
<Plan plan={1} color="lightblue"/>


<!-- Spheres bleues-->
<Link {...link1}/>
<Link {...link2}/>
<Link {...link3}/>