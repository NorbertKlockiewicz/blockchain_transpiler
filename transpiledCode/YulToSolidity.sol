contract Token
{
    sstore(0,caller())
    caller()
    datacopy(0,dataoffset("runtime"),datasize("runtime"))
    dataoffset("runtime")
    datasize("runtime")
    return(0,datasize("runtime"))
    datasize("runtime")
}
contract runtime
{
    require(iszero(callvalue()))
    iszero(callvalue())
    callvalue()
    if (selector() == 0x70a08231)
    {
        returnUint(balanceOf(decodeAsAddress(0)))
        balanceOf(decodeAsAddress(0))
        decodeAsAddress(0)
    }
    if (selector() == 0x18160ddd)
    {
        returnUint(totalSupply())
        totalSupply()
    }
    if (selector() == 0xa9059cbb)
    {
        transfer(decodeAsAddress(0),decodeAsUint(1))
        decodeAsAddress(0)
        decodeAsUint(1)
        returnTrue()
    }
    if (selector() == 0x23b872dd)
    {
        transferFrom(decodeAsAddress(0),decodeAsAddress(1),decodeAsUint(2))
        decodeAsAddress(0)
        decodeAsAddress(1)
        decodeAsUint(2)
        returnTrue()
    }
    if (selector() == 0x095ea7b3)
    {
        approve(decodeAsAddress(0),decodeAsUint(1))
        decodeAsAddress(0)
        decodeAsUint(1)
        returnTrue()
    }
    if (selector() == 0xdd62ed3e)
    {
        returnUint(allowance(decodeAsAddress(0),decodeAsAddress(1)))
        allowance(decodeAsAddress(0),decodeAsAddress(1))
        decodeAsAddress(0)
        decodeAsAddress(1)
    }
    if (selector() == 0x40c10f19)
    {
        mint(decodeAsAddress(0),decodeAsUint(1))
        decodeAsAddress(0)
        decodeAsUint(1)
        returnTrue()
    }
    else
    {
        revert(0,0)
    }
    function mint(account,amount) public
    {
        require(calledByOwner())
        calledByOwner()
        mintTokens(amount)
        addToBalance(account,amount)
        emitTransfer(0,account,amount)
    }
    function transfer(to,amount) public
    {
        executeTransfer(caller(),to,amount)
        caller()
    }
    function approve(spender,amount) public
    {
        revertIfZeroAddress(spender)
        setAllowance(caller(),spender,amount)
        caller()
        emitApproval(caller(),spender,amount)
        caller()
    }
    function transferFrom(from,to,amount) public
    {
        decreaseAllowanceBy(from,caller(),amount)
        caller()
        executeTransfer(from,to,amount)
    }
    function executeTransfer(from,to,amount) public
    {
        revertIfZeroAddress(to)
        deductFromBalance(from,amount)
        addToBalance(to,amount)
        emitTransfer(from,to,amount)
    }
    function selector() public returns (s)
    {
        string public s = div(calldataload(0),0x100000000000000000000000000000000000000000000000000000000);
        div(calldataload(0),0x100000000000000000000000000000000000000000000000000000000)
        calldataload(0)
    }
    function decodeAsAddress(offset) public returns (v)
    {
        string public v = decodeAsUint(offset);
        decodeAsUint(offset)
        if (
        iszero(iszero(and(v,not(0xffffffffffffffffffffffffffffffffffffffff))))
        iszero(and(v,not(0xffffffffffffffffffffffffffffffffffffffff)))
        and(v,not(0xffffffffffffffffffffffffffffffffffffffff))
        not(0xffffffffffffffffffffffffffffffffffffffff)
        )
        {
            revert(0,0)
        }
    }
    function decodeAsUint(offset) public returns (v)
    {
        string public pos = add(4,mul(offset,0x20));
        add(4,mul(offset,0x20))
        mul(offset,0x20)
        if (
        lt(calldatasize(),add(pos,0x20))
        calldatasize()
        add(pos,0x20)
        )
        {
            revert(0,0)
        }
        string public v = calldataload(pos);
        calldataload(pos)
    }
    function returnUint(v) public
    {
        mstore(0,v)
        return(0,0x20)
    }
    function returnTrue() public
    {
        returnUint(1)
    }
    function emitTransfer(from,to,amount) public
    {
        string public signatureHash = 0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef;
        emitEvent(signatureHash,from,to,amount)
    }
    function emitApproval(from,spender,amount) public
    {
        string public signatureHash = 0x8c5be1e5ebec7d5bd14f71427d1e84f3dd0314c0f7b2291e5b200ac8c7c3b925;
        emitEvent(signatureHash,from,spender,amount)
    }
    function emitEvent(signatureHash,indexed1,indexed2,nonIndexed) public
    {
        mstore(0,nonIndexed)
        log3(0,0x20,signatureHash,indexed1,indexed2)
    }
    function ownerPos() public returns (p)
    {
        string public p = 0;
    }
    function totalSupplyPos() public returns (p)
    {
        string public p = 1;
    }
    function accountToStorageOffset(account) public returns (offset)
    {
        string public offset = add(0x1000,account);
        add(0x1000,account)
    }
    function allowanceStorageOffset(account,spender) public returns (offset)
    {
        string public offset = accountToStorageOffset(account);
        accountToStorageOffset(account)
        mstore(0,offset)
        mstore(0x20,spender)
        string public offset = keccak256(0,0x40);
        keccak256(0,0x40)
    }
    function owner() public returns (o)
    {
        string public o = sload(ownerPos());
        sload(ownerPos())
        ownerPos()
    }
    function totalSupply() public returns (supply)
    {
        string public supply = sload(totalSupplyPos());
        sload(totalSupplyPos())
        totalSupplyPos()
    }
    function mintTokens(amount) public
    {
        sstore(totalSupplyPos(),safeAdd(totalSupply(),amount))
        totalSupplyPos()
        safeAdd(totalSupply(),amount)
        totalSupply()
    }
    function balanceOf(account) public returns (bal)
    {
        string public bal = sload(accountToStorageOffset(account));
        sload(accountToStorageOffset(account))
        accountToStorageOffset(account)
    }
    function addToBalance(account,amount) public
    {
        string public offset = accountToStorageOffset(account);
        accountToStorageOffset(account)
        sstore(offset,safeAdd(sload(offset),amount))
        safeAdd(sload(offset),amount)
        sload(offset)
    }
    function deductFromBalance(account,amount) public
    {
        string public offset = accountToStorageOffset(account);
        accountToStorageOffset(account)
        string public bal = sload(offset);
        sload(offset)
        require(lte(amount,bal))
        lte(amount,bal)
        sstore(offset,sub(bal,amount))
        sub(bal,amount)
    }
    function allowance(account,spender) public returns (amount)
    {
        string public amount = sload(allowanceStorageOffset(account,spender));
        sload(allowanceStorageOffset(account,spender))
        allowanceStorageOffset(account,spender)
    }
    function setAllowance(account,spender,amount) public
    {
        sstore(allowanceStorageOffset(account,spender),amount)
        allowanceStorageOffset(account,spender)
    }
    function decreaseAllowanceBy(account,spender,amount) public
    {
        string public offset = allowanceStorageOffset(account,spender);
        allowanceStorageOffset(account,spender)
        string public currentAllowance = sload(offset);
        sload(offset)
        require(lte(amount,currentAllowance))
        lte(amount,currentAllowance)
        sstore(offset,sub(currentAllowance,amount))
        sub(currentAllowance,amount)
    }
    function lte(a,b) public returns (r)
    {
        string public r = iszero(gt(a,b));
        iszero(gt(a,b))
        gt(a,b)
    }
    function gte(a,b) public returns (r)
    {
        string public r = iszero(lt(a,b));
        iszero(lt(a,b))
        lt(a,b)
    }
    function safeAdd(a,b) public returns (r)
    {
        string public r = add(a,b);
        add(a,b)
        if (
        or(lt(r,a),lt(r,b))
        lt(r,a)
        lt(r,b)
        )
        {
            revert(0,0)
        }
    }
    function calledByOwner() public returns (cbo)
    {
        string public cbo = eq(owner(),caller());
        eq(owner(),caller())
        owner()
        caller()
    }
    function revertIfZeroAddress(addr) public
    {
        require(addr)
    }
    function require(condition) public
    {
        if (
        iszero(condition)
        )
        {
            revert(0,0)
        }
    }
}