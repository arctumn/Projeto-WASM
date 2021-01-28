(module
  (func $mulby2 (param f32) (result f32) ;; nome_funcao param_in param_out
    local.get 0 ;; param num 0
    f32.const 2
    f32.mul ;; multiplica os elementos atras mul apenas aceita dois argumentos
  )  
  (func (export "sum") (result f32) ;; export para JS param_out
    f32.const 5
    call $mulby2 ;; multiplica 5 por 2
   )
)
