object "MyContract" {
  code {
    // this is the constructor.
    // store the creator in the first storage slot
    sstore(0, caller())
    // now return the runtime code using the special functions
    let x:=datacopy(0, dataoffset("runtime"), datasize("runtime"))
    return(0, datasize("runtime"))
  }
  object "runtime" {
    code {
      // runtime - just return the creator
      mstore(0, sload(0))
      return(0, 0x20)
    }
  }
}
// this is example of core yul contract
// It should contain object NameOfContract
// code {} is the constructor
// object "runtime" is the runtime function