// Auto generated kernel

__kernel void log1p_float(__global float *src_0, __global float* dst)
{
	int gid = get_global_id(0);
	dst[gid] = log1p(src_0[gid]);
}
