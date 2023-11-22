import type { Vector3 } from 'three';
type Link = {
	source: Vector3;
    destination: Vector3;
    color : string;
}

export type Links = Array<Link | null>