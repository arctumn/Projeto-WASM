(module
  (type (;0;) (func (param f32) (result f32)))
  (type (;1;) (func (result f32)))
  (func (;0;) (type 0) (param f32) (result f32)
    local.get 0
    f32.const 0x1p+1 (;=2;)
    f32.mul)
  (func (;1;) (type 1) (result f32)
    f32.const 0x1.4p+2 (;=5;)
    call 0)
  (export "sum" (func 1)))
