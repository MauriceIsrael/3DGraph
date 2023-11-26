<script lang="ts">

import { onMount } from 'svelte'
import type { Contributions } from '$lib/type';
import { Octokit } from "@octokit/core";
import { T } from '@threlte/core'
import { Align, Grid, OrbitControls } from '@threlte/extras'

// Octokit.js
// https://github.com/octokit/core.js#readme
const octokit = new Octokit({auth: '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'})
let response = {}

let contributions: Contributions[] = [] 
onMount(async () => {
    response = await octokit.request('GET /repos/{owner}/{repo}/commits', {
    owner: 'MauriceIsrael',
    repo: '3DGraph',
    headers: {
        'X-GitHub-Api-Version': '2022-11-28'
            }
        })
    })
    console.log('authN réussie!')
	console.log(JSON.stringify(response))

</script>


<Grid
	infiniteGrid
	sectionColor="#4a4b4a"
	sectionSize={20}
	cellSize={20}
	fadeDistance={400}
/>

<T.PerspectiveCamera makeDefault position={[10, 100, 100]} fov={60}>
	<OrbitControls enableDamping  />
</T.PerspectiveCamera>

<T.AmbientLight color="#fff" intensity={0.4} />
<T.DirectionalLight position={[0, 200, 200]} intensity={2} color="#fff" />
<T.DirectionalLight position={[0, 200, -200]} color="#fff" intensity={2} />

<Align auto position.y={100}>
	{#each contributions as row, i}
		{#each row as day, j}
			{#if day}
				<T.Group position={[0, 0, 12 * i]}>
					<T.Mesh position={[12 * j, day.count / 2, 0]}>
						<T.BoxGeometry args={[10, day.count, 10]} />
						<T.MeshStandardMaterial color="#fff" />
					</T.Mesh>
				</T.Group>
			{/if}
		{/each}
	{/each}
</Align>