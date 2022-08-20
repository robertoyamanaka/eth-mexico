from gpt import Example


def add_graphQL_examples(gpt):
    ### Premia Mainnet
    gpt.add_example(
        Example(
            "Give me the id, name, symbols and decimals from the first 5 tokens in the premia mainnet subgraph",
            "premia-mainnet{tokens(first: 5) {id,name,symbol,decimals}}",
        )
    )
    gpt.add_example(
        Example(
            "Could you please give me the id, name, the id from base and the id from underlying from the first 10 tokenPairs in the premia mainnet subgraph",
            "premia-mainnet{tokenPairs(first: 10) {id,name,base{id},underlying{id}}}",
        )
    )
    ### LivePeer
    gpt.add_example(
        Example(
            "fetch me the id, inflation, inflation change and max earnings claims rounds from the first 6 protocols in the livepeer subgraph",
            "livepeer{protocols(first: 6) {id,inflation,inflationChange,maxEarningsClaimsRounds}}",
        )
    )
    gpt.add_example(
        Example(
            "could you provide me the id, activation round, deactivation round and last active stake update round from the first 2 transcoders in the livepeer subgraph",
            "livepeer{transcoders(first: 2) {id,activationRound,deactivationRound,lastActiveStakeUpdateRound}}",
        )
    )

    # Rai Mainnet (aqui empezaste a testear las queries)
    gpt.add_example(
        Example(
            "could you provide me the id, address, id for the proxies and if for the safes for the first 5 users in the rai mainnet subgraph",
            "rai-mainnet{users(first: 5) {id,address,proxies{id},safes{id}}}",
        )
    )

    # Audius Mainnet

    gpt.add_example(
        Example(
            "give me the id, audius token address, claims manager address and delegate manager address for the first audius network in the audius mainnet subgraph",
            "audius-mainnet{audiusNetworks(first: 1) {id,audiusTokenAddress,claimsManagerAddress,delegateManagerAddress}}",
        )
    )

    # Connext Network

    gpt.add_example(
        Example(
            "Please give me the id, amount, id for the router and asset id for the first 5 asset balances in the connext network subgraph",
            "connext-network{assetBalances(first: 5) {id,amount,router{id},assetId}}",
        )
    )
    gpt.add_example(
        Example(
            "Could you give me the id,id for the asset balances and id for the transactions from the first 4 routers in the connext network subgraph",
            "connext-network{routers(first: 4) {id,assetBalances{id},transactions{id}}}",
        )
    )

    # Sushi Mainnet

    gpt.add_example(
        Example(
            "Fetch me the id and id for the liquidity positions from the first 8 users in the sushi mainnet subgraph",
            "sushi-mainnet{users(first: 8) {id,liquidityPositions{id}}}",
        )
    )
    gpt.add_example(
        Example(
            "provide me the id and eth price for the first 17 bundles in the sushi mainnet subgraph",
            "sushi-mainnet{bundles(first: 17) {id,ethPrice}}",
        )
    )

    # UMA Mainnet

    gpt.add_example(
        Example(
            "give me the id, address, count reveals and count retrievals for the first 2 users in the UMA mainnet subgraph",
            "uma-mainnetx{users(first: 2) {id,address,countReveals,countRetrievals}}",
        )
    )
    gpt.add_example(
        Example(
            "give me the id, if it is supported and id for the price requests for the first 6 price identifiers in the UMA mainnet subgraph",
            "uma-mainnet{priceIdentifiers(first: 6) {id,isSupported,priceRequests{id}}}",
        )
    )

    # PoolTogether
    gpt.add_example(
        Example(
            "provide me the id, owner, id for the players and id for the balance drips from the first 8 comptrollers in the pooltogether subgraph",
            "pooltogether{comptrollers(first: 8) {id,owner,players{id},balanceDrips{id}}}",
        )
    )
    gpt.add_example(
        Example(
            "give me the id and id for the prize pool for the first 3 sablier streams in the pooltogether subgraph",
            "pooltogether{sablierStreams(first: 3) {id,prizePool{id}}}",
        )
    )

    # mStable Protocol
    gpt.add_example(
        Example(
            "give me the id, exact, decimals and simple for the first 7 metrics in the mStable protocol subgraph",
            "mstable-protocol{metrics(first: 7) {id,exact,decimals,simple}}",
        )
    )
    gpt.add_example(
        Example(
            "give me the id, address, decimals and name for the first 5 tokens in the mStable protocol subgraph",
            "mstable-protocol{tokens(first: 5) {id,address,decimals,name}}",
        )
    )
    # Synthetix Mainnet
    gpt.add_example(
        Example(
            "pass me the id and proxy address for the first 4 synth by currency keys in synthetix mainnet subgraph",
            "synthetix-mainnet{synthByCurrencyKeys(first: 4) {id,proxyAddress}}",
        )
    )
    gpt.add_example(
        Example(
            "could you give me the id,name and symbol from the first 14 synths in synthetix mainnet subgraph",
            "synthetix-mainnet{synths(first: 14) {id,name,symbol}}",
        )
    )

    # DodoEx V2
    gpt.add_example(
        Example(
            "give me the id, pair count, token count and crowdpooling count from the first 7 dodo zoos in the dodoex v2 subgraph",
            "dodoex-v2{dodoZoos(first: 7) {id,pairCount,tokenCount,crowdpoolingCount}}",
        )
    )

    # Hop Protocol Mainnet

    gpt.add_example(
        Example(
            "please give me the id, new bonder, the id from the block and the id from the transaction from the first 8 bonder addeds in the Hop protocol mainnet subgraph",
            "hop-protocol-mainnet{bonderAddeds(first: 8) {id,newBonder,block{id},transaction{id}}}",
        )
    )
    gpt.add_example(
        Example(
            "please give me the id, previous bonder, the id from the block and the id from the transaction from the first 6 bonder removeds in the Hop protocol mainnet subgraph",
            "hop-protocol-mainnet{bonderRemoveds(first: 6) {id,previousBonder,block{id},transaction{id}}}",
        )
    )

    # Uniswap V2
    gpt.add_example(
        Example(
            "give me the id, id and symbol from token 0, id and symbol from token 1, reserve USD and volume USD for the first 6 pairs where the reserver USD is greater than 1 million and the volume USD is greater than 50k, ordered by reserve USD descending in the uniswap v2 subgraph",
            "uniswap-v2{pairs(first: 6, where: {reserveUSD_gt: '1000000', volumeUSD_gt: '50000'}, orderBy: reserveUSD, orderDirection: desc) {id,token0{id,symbol},token1{id,symbol},reserveUSD,volumeUSD}}",
        )
    )
    gpt.add_example(
        Example(
            "give me the reserve USD for the first 9 pairs where the reserve Eth is greater than 100k order by reserve USD descending in the uniswap v2 subgraph",
            "uniswap-v2{pairs(first: 9, where: {reserveETH_gt: '100000'}, orderBy: reserveETH, orderDirection: desc) {reserveUSD}}",
        )
    )

    # Doodle Bucket Auction
    gpt.add_example(
        Example(
            "give me the id, bidder, bid amount and block for the first 8 bids where the bid amount is greater than 100k order by bid amount descending in the doodle bucket auction subgraph",
            "doodle-bucket-auction{bids(first: 8, where: {bidAmount_gt: '100000'}, orderBy: bidAmount, orderDirection: desc) {id,bidder,bidAmount,block{id}}}",
        )
    )
    # PolkaBridge AMM
    gpt.add_example(
        Example(
            "give me the id, pair count and total volume Eth for the first 8 polkabridge Amm Factories in the PolkaBridge AMM subgraph",
            "polkabridge-amm{polkabridgeAmmFactories(first: 8) {id,pairCount,totalVolumeETH}}",
        )
    )
