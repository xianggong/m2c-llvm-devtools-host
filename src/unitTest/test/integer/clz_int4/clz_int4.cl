// Auto generated kernel

__kernel void clz_int4(__global int4 *src_0, __global int4* dst)
{
	int gid = get_global_id(0);
	dst[gid] = clz(src_0[gid]);
}
