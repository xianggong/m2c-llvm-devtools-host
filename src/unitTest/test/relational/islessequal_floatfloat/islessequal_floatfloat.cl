// Auto generated kernel

__kernel void islessequal_floatfloat(__global float *src_0, __global float *src_1, __global int* dst)
{
	int gid = get_global_id(0);
	dst[gid] = (int)(islessequal(src_0[gid], src_1[gid]));
}