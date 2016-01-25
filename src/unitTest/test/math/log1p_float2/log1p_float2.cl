// Auto generated kernel

__kernel void log1p_float2(__global float2 *src_0, __global float2* dst)
{
	int gid = get_global_id(0);
	dst[gid] = log1p(src_0[gid]);
}
