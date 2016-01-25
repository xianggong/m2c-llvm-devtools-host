// Auto generated kernel

__kernel void fmin_float8(__global float8 *src_0, __global float8* dst)
{
	int gid = get_global_id(0);
	dst[gid] = fmin(src_0[gid]);
}
