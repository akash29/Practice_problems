def number_needed(a,b):
    charac_dict = {}
    to_delete = 0
    for i in a:
        if i not in charac_dict:
            charac_dict[i] = 1
        else:
            charac_dict[i] += 1
    for j in b:
        if j not in charac_dict:
            to_delete += 1
        elif j in charac_dict:
            charac_dict[j] -= 1

    for k, v in charac_dict.items():
        to_delete+=abs(charac_dict[k])
    return to_delete

a = "pxavnqfmhmgdleebjbcihnlfhrvgrgjgdlbsdiflwloirulawnkfaymjpkpiqapvmsnrduczhthynsblgnsilfsdpjlhkccyxrpaoszxnhyazbohogqcnifcrsldvpbsjrsxlrwyauaavojkxzokjtpbnaeiqiczzwykqukqpksmbewydmkpfzqvawdsgirfgpryjdraqlnrplrvydkfdcafagxhqoowfgvqlorbzguprnkrruzuwzbwhydxmswtarjnhcpgilvczftqbsmxunwbnbzbtvuvodjvgadolzskgmcigqhcfdesfftacnyqtjnbjqpwrkjywlieerhjvnccsxeulcmglbhwtytliclgpvltmufjhjnzgsvtuhziiggbfzopdbwvwhqldvukeillagewnggxmpatqpjusfprohcrdwdhgouiwbhlhnitckptzypufgltnnmslrcshwadxjoexyabipwkpneuvrpjebdpufjbcmgbvwiuukyebwoqkumflbqreujybsbdghhcdpwzbwfctwsfqgmehdxnzgncboghxplcgkdhgijzedgxjtdsyafzjsbkijtfyfhepklxuwzzzfwiybcwbhxmbzyjisqjzznolbngxmfzsdjqgmphvmwxnugwmzfnyubkxpqvbxwvcfoitfrptnmhiudwtkksenceeubirxdtetbyyunsibzsveoroaluopysjzccygvdzybasqsctruqvjhllshzhgushwugerlgpogkeymxrjnosxzdrgfbobtwxoeefrkxfsjlqxijgxxawwgoelpvoitlyxrgobdvtogllquuntukraawnprbzmpyjggzkjwfzcrksnghhbtadtwrkpukblkmsqnebjjancmfsvpbwibzcasorpavakhucxyfikhwoudgrsjnblofnjveywzyijvlivqqfyowusclmoapzoumxssvoswwdtjloadwasswmwhykjolxkxxcsuqmspplyacadyaxqwjmfizoykoiknnchdoaudntfptknwifurucbtszdgkntxrdcfdxkqspgncvjkbgdvifqagthqjcpafsikrudjmlyogkyhqdeyiuyrqhjzmzbtrlekghvsstiadiitlotwjsnzbwanvbjopnavwvpqpxqufaoqpjmabbzfybuvedktqkooidezaxthxjyotmowopbmqwhvztosgfiqkppnmiulusanfqjtgnhyjqvkmmeurnkbczqqjlbdddskwcferocahamtmtndgzgkyxcjkfnnjfafjhjawncdnryzknesmnemmgvwlklwsndbvoetciyrzwtljxdxmhjypewbrkzjxdmurqnvblnajgoufrrsbasqhrtybtjyyvtpoinpuapfidapxrhaucqdvmbwfmwfhpwvajkwlcbthbjgvsgpwxsrlvpshmxqbtoddyzocbkkevszpzqmykfjhvbohyhkrvowvnlyqxkvscujbnxbxdkfalvjlctdzjzvzmtpjfmdhjnlwkmtpzapkyywaubcdcxepqwaxieertrpdgjtflipjjnmdqoitlnidlkatqgnjacngnilzqckbqyegmnbzcjenwgimpvwpylvltimlkzncxrlmgmlkysxuyigpdeedpbrilfuwehyeajqhybrwvrqwbyledskstddfixdpedtgpjnnmhjiazebzphcjrxduakfxpudsnjhwzuiifqiewjeoqixkfaghmlgbfjwsvfowazefrmmoxscnczzkcgrqryuxjqreviaxhefystopnsfpsezwktmergdayuhwejtlqamktcagvfwplxlyqzcjghmgbvcieytwahhumhchoawzyjzqibaqimxmjbwnbrmcztwncyuszstzbtrjwrahfzvoareciqejlcwpcshdkcenvwxsnzbvywlanpevhifumbjpwsugvzusvtmkunhsjtuwkzuujboweanauhjridmdyyqsmxmxsiwdhqxrtnpxpeymlhdwmpzmorgcpuzhcxmkpldibugqyeclnihbxjnnatppnrzpqlbgxgoyauqaatmnbtoacdofwfulyvdphevgnjgnewogrcwuvmvaqlfoqbarxdgejbmwmsmsoczgevabjxbziiozkqqhtynebzbntnihrjpvgqwpnaryifzuxpdspqwqrzfkopufyjaebzwrznphuocrffjwyhorhvevlydljdqlcoedbtlvjpmqwxmueaonvsjismubrmmwaszblmwwdkmahawnakbyemgwaayrompofppsdnphxdjgefugsxewjnvjptcefsskjifmvuvvxebdmvkesocdbxmrqrxyjpkuxpgvleqjitowpycjnfnqebjxsgvdyhxxxgskmkvwektvivgxcvqhzzeribxgiwdhcysoknlqxglibufepvloxrifshncdqkiqewbtjrtpfbtzgxqekhbbrgtavxdlhlenkfjvyclddeeldxpngsozyjztgchqqnfasovqqiwvocjrzaehtugtffnmkwealjcdyxvqitmwwxoxxufqplkutzidxmdiyhnwekooealczbzxvgpmszjnarqxgvhgcueifsxlvinulorgvhtpiecjxuidpqltmpbtiaedktxvkrchyxwgbaryuaelspeehhypiessarokisrgpppspiqliwyaoefvlfktjeolvcveuomldddumvhwufxijefvlpqwvgisidweulrxquucsbzojywsebppsilpothzzgftrxshtomnsnbblxvpanguvrjlnrkmxshqpbziqlwkazllzgcztiwqchcpyodxgmnxnpifcgpdfcqejtgedcxhjzykpbhypxvfodmqjctpgktrfbwkdtspuqzluijjhfovkdoufjlntgfaidnnyfcsxdftopfvwvtgyjcfsptowyogdbtbiyvibabrrgpneiwctyilqbzmbquetnhencmrepiwyxjchheaiooyppmshgybvfhjhvamkiikitmpbtqjhgjzvvrdbqgyxnhfijtuudfcyrtzmjkurtvnooqrewqelzjtlenhhsjfmehyqruhnpubekvkinotmzozdcgmwruiwbjmudthtolzagjltyehzthdxnrtfledmnphqiqlybkzjwmewsmvlvakisgpdksszhbpsrdqvprgnfljyzfluhwczcufomxnwaeqthiozaxmfiwfhdrbmnfmrztfossmswclgkchmztuhrzqwqrjfyxwyqdoivacuenaqrhfqczzwarutidyhcxhuaxcyzgsdwuvndagfbhdezyxjdxsgubaxyfvxlncjhyxmafrcoxgnvfzacrgztjytqtrditnrtmdutwyhtgxqlwrpnzqikqcajvgtqtkkhpgamgjhmgazctqsshafzehjznesirergkruqdeejedmztercgyclgnmvtegkixturpmuvsdbvrarvuveszpaodwkkeusbppshbmcuqgrjgkhailvhcvyftipxekzuztdcghyynshucowkbrudpsliaaigmjcncfsinqickqwngvzimtnbnympbuwndybfgtqvlyxwqwlzrkjfgwjvvvlwrjlujmbrhrmvsmtkiejbqsiyprumohifsvbbidvrwhoqvhbdlmgehrcyiwkxfuexpgbzlytjfhcbpdgcrpgygjwqhgppcuoscrtppmyvucyjfgnzvuxdfwuocjdhfsbhjuwzhxwbbwmheziavffabzpglupqoqyykwzrvxsxvggziobdvhgzixhtrwkgmkgwifogeifzplyzbacyjixrfelzaxfmjnjruzzyhexypxxszcrimqasvntxmakvnvohwohdueemddedfxnsopmlehiqhunwrednumtoszavcfakeocudqhixsygmocgshvmtoclpdgskhcoxglaysixkjdzxffrmafhrhsgkaaujelgkwhkqrhbckazrhsdhxmafejrhjoqobzazilpbsqefsfwzycjvojcvswcemusnvsmffdhaulfoqboodzmuiqpdothapbplvbqbhzbdkgrdjhrpgfjryaumtdpkeexbiqcppfsanjfxrwoxezqczkqupfevkexuuzjjhblumqtfphftgvxhgnbxvithmqbirktanhvzxqfoykjghgqnwrnrbgypybzrltsyapzzfgofsxmagcpevcxzkxqiyqcjjujjjkkqrywjyklgobklfjmqgdyetcpewaphmzadawpygcgwdshjbuzjxzpseeyagnksokyoipoorwmxotippjaokpiovgpbvbwmnwavnrlenxdeslviuwyflhthnkklngxaezvrsgygfbkyphijdgqpnkwdwgokpnmtoinhqlpwobwdiepmkfbarxfqftawimswwfdpssngtjmcpbqbgrbaqgqxbsulgmidrnulihrdqfhhgxipomrguhewzyjhktkdhgornhudncmvzvkohbubkazlyjticfnlmbczjxfybrtameqvhnxsnydmhywmekzqlcrwbwucooccuvybixvvvbjfzgtdssvfwncxjwzzmeegzekjdfgygqfiyylqtjvpwznhyojksnrtrdewilurbczbcktvtqlrqyzooiajxrcqwjmfuiwxkxynhtkdjvwzvvpkfqtejxuggglapjzbgxqpsbucwrdsotewjzaswvafdnhuwhyegowzpqdojgiazmyinydjvdqbryvphvwnksobkrpwyxwxlwiywnkssavjasbhoxxyrlzbdrzdqxcctkcqzmkspfdpxezndwluhnymezpuxsyqebiepswgxzyxgxkltyiclirrhgneamxhpflgyjpxknwqmjehhmluucnblaglodsfkfmiodizserenvnwhyqdbdfognzusuacbonqtvrlzkrpielreevhhcvppxmjronueamxvdixqbmyfxplbmtloocflooeccbgenfarpxjqlhxkyjolebbsdhguxmwbnfgdmiwchfusoucmfqzjtddxklrjypnnwvqldmpktjehfiwkbvtuyxtkimwicjwaeonjdcvwmzerhaeixxfyuykflgnprlrvcfefhzdvahpkjtsjqzhnyrslaharvrnzwteevjzxrohchclabsnbmhmmqmdngsmcoqglaiitysxiujixdxzrgldwajkgdwkrpterbnmbhjjbutyyqzrwnvvnghvjdfduyhnbwzddlogfihfagxztuuiabflglqdlaqpwsscdikiqrqranqtjmelpjyxwpakptznlrpqzcastqltfbpopvbeeaddpgnezmtmflegneyivjccmttdouhuunxltmruylgdwkmjqkrnwvqkqjoefxbakynflfzlqhrmrdxknqxlopweamlgjmiwmvbzablqicecfdmuwlikbeqbqdhbppxenzdncqgkumobsawomganksqcwyfnpfrcgxsinasimjlejjuxpumbpddldlysqqxwnpecrymdhyktheqxbfyqiedlrbfhtcditjlkjzqtxcmhiegljgbtkgebimkdopmkazwkymdyorhzvnkhtoaguhjetuijlwvmvsyvebvvucurpgylubrpkatfwdqkzmwueuskxnhrqdihkjsekjvwmpbkuruudqojmiujwbamfltrumvextajkdueuqyahpjtxffthfhoqbfmpcqoxsyhxumukkutzfpzlusubaiudpgstzgttgarcmlpzhiaoxzzrstvudpxuvrquzjoijhkyubxbkzpjzrdtmypsnmmkfehgnvozebzycyboxsyyjdtybiqqweablhkaeabibaigyjuyeuwpxqnaafqxmraxakzhlbrobauclrcrnahnswntceqqxqpzdogoryetabxnszfhzmusiinmodenvtmakvobtvwvwtiounxwzsqkcdysidhfwtgiqwklrignepdycbwevmozrorzryhqtnykjkvbtcoxtsvxvubqgrpagibziipbvonfyjirnwoiqmflgjbocsqiasiiazmynzfmknfzlwhcipnqyrgajxlkrvutugrkiyyulfuxbdblsobsfkvrjidafxvbgplqnlkbrgaskbeerhzztuqcctejsakapwqejdfalftxizcaibzcxpgbklkcnufesvkcaqemxxjgynghqflpwrqgecktzpztnkxpacbxbnfaaljtsuiqnbwudjneynynxvdzxeyztebwrkpmgzctabngmdkkskypgbqfhqeduhzorqcxpgtshgytlkgdvgudjkisdpvxwunqmpncygwfpwbagjgdpaganrsqiopekfuxwkbusxchtfkboqffsnffgzvopnvasrzobajuzndssntgfanyoufutdllqglixmyzojvnwyhooawvdjtrfznbcymugzeelcfzoaokavbqxxmajftogjrkjdeqckupnbqdbepdzquxqgzbntrwcjgnmndrxzgmaxpddfjdxdcnldqawiwardofstwptfcvcrzfykkynolaseaqmzrfchmuallvqnruhsbhcofrctruxtnlseswlesnpejhtabcufkwtrpvkisjbhuwlmuyrnnitwqmytrsybqtsfrfnlorsjndxhdqwqzpprenmvinwygqexvrimiavxfshklddktsdxhpspcqojiuigntsyvpvbjcnugqebijyqzsfdkvospxydssbnhyqrdellusmdbmvcecgoywipvhsnbvbjwrczvnkqhwvlisnouveusmknvebxcegyviztxjlhhisrafhwblrvxbkvhnsjrajpkiijttqcbivdoczrpsonvykdmcofcyuoicxexogawefmgffyxtnvuxyizondoktxoqdmglodpurybxwasjvmgvuhkkkyudxivaucmlhdfybivxiqiecozxvlhhmdmllimikatrdarhineqdpwhdygbjpixsvjefxmrxhicjzlroqjtfgdkejlpzwpttyxyxlpwuzydakurcemjmpvsbjjcfyvaytyvgprbqqgqcbjghwrvnmnovwqcvocvjcrptisjazacclkjhbexqtnnpesmuwidzzssjnckmeoqrzbzchyualkrrcelyoozpjsywwikcxatyducksxkehbxlhjjxxlmgdlebvqdusysvtvfnurtdvroeazczkoipboqxfvrxumvpjacduyippwtrxxskoazrrsowpivlwqaftfkndseuqznnxfznibeztvxkfswblyigfstikzeayrpxxpmhqrglmfxrztukucqzulkgmoinixkhoxogqwrcbpvakpnetfgptqvfgdsocfvtelzuhtykkvnwmadfhjucbrihwcyajvtpjvjqojbygqusqxzzivcjmmtkqtlaogpxbbqpmtptjmnblnaukefzsyjjrwjidahebxuqqljbxycjnfdylkzejinchymkyuocrkskwdntdqerxjpiuoodybhfburcoiehuytqdhmgzsxycogwexbfyimcceesokaiivbncptdhtbjjkfqhgvhrjjvpnodxqmhlpwqeqtllvvwhcmojjvcthxiuloudadppahtsagdxbbeeoupzqrsxodtcrpfrtwitddlgjqfnrkrheghwzbvperrvgzobvyubbhhnxmarytyfbhdajzppsjlyizafywgbenqdcqualvhmelonkefepqcxrecrdlthalkcchfpemcixqyjwdpltukkypcdaxmaizfmgmekygsyyqjvvziotvbtmfzmelookvdshhcipxinptklutbpqcjcjkqnvgcgchylodtdcdqrxberwghoisqucihzolhssgeglzlndegahltdratbulvytfyjqfcjngrafdnkjwkqhgvaiobdzzbuebdujffwnzxtemdniqdrwyremvjnunhyokuxsawfbvafhgsswvlutdahymwuzdsppophqlpripwrvojtlvpgasnyejudomsgchptuemcwjutzfpncetcwjccuwfjkappjgigluijfechmruowntuwvxruecggtvqzdymagvhnyozrkpnyikwgjpaptgwocoqhmcjuathahiruyhuitqociqrdxpsbdikpmukmntmwcgqcnkmgdbknrdqqtkrwucmhywvnpkjtqcxdokltlvieybvtloqgscpqakdruplktipjucdfznmaohtcxjiqnzgnjmfedsqwcgfxikeiyqiozdqxnapazxqjjvnopdmrlsqwevgenqtptjogmdjlazumwjcnppgcjxynueuhunwqymykphysiugeeitvxaxgxywrcqazfzrdlpqbxqvhkboqjhljhlpejnxndyoizfokxgnwwidglrzxzmggxxnilkyokozjwputvjptssbdkaajnirmgevtrvjbjilfzhauqppkkrqutsfgdytjdqcullxwwkevtesmwhwgaocujjcmhxxmpziamgzkqdgmjayfjwlmnniwwkigkfszgbcuhbfzgnlpplvyiimvyutufdarkvqswsmfvtgbgutxfqwpykmwfftmivduqtmmoztjsanbugyzwwrwhdtmjmythdoawaokbiwwijxerxdpwwldaerlsrecuuesxsfycbummtqfrwunsfssmldgekiygmsdhxejaawoumtnkpcdxwxlhbrlncltqfzxffhfffwbtrqejshgqetzhkmwoxsffrckylrdsnhmhxqqszyifrkpbwlqudxbwzluncahqjtzglpamnluevjhrwznawoyyzvlcxsugotozkpoxaidxrkonkepgsqeunrykmuqapgbzvpwxzbuqllgxpxejpkfccdmoxeqmlrnijliimcbypjvggbswmxaqdngatwpgpcpyqxjcbkcttazbbrzprahupnwijnrzsizihikiundnpdrqwqipqpjfdiqovhnpppxwxkgszkhopygnrodhgonjwfzumnjbehzbrfvspfggfmuwbzehntsmyrgmgppkyoortljlqrtwenshmyoctiotbufkluumikfeyrroikmmahtmhjobteuvaafmwbafohlmycchopvoyrdfctgwybtydamzbogrwtduvidmxzavsfcuzjqxmlxrlkqpyzgusmrquuctveqnksijdaipmfixpbmqavmshdkdamyvtojditomtwdfdmfvptlpozjxducdiaadqjizewnyusfygmtvggkufwukswpczqgpboqgndghylheaccgiocqkwaevshuknjldctqfzafnhmnkotucxkpwntrhalrpwcvywngxpnkxzzjnsfssshohafodsfuqjrphfxfukrtkrezlkrdearldyzgqgchrwyzdxgxhxttqzvclmhpnzaqzbyqjczbyzabwibdhwzyvuahijwxkznkancksbnqanuwxxbetccqwexhoweyxuixhkjbnwsplolilpngrrwqwwxmsbkpvvofhagxyamkqyubpjhgbgwzctlwxxluubbcdkzckloblkeauojxufwwbjuygfsbiufmegqqtgtfqyhmoqjkyhizqcxzjpcrlhfppviidbpubxgppqznzhosjlrsdvmoetgtroburtotsvihnkxmtlgfzxzcunsyhyryovsgojzgejptvohpaowbnxdilviswasmxksntttzfkuazcrbspchnhryeascckpzujmqfhrktmmsqgvkxzrkgjknlcpnmgmjsabxjsjcgxxwfsiducnclypychlpnxafzbeitnmcnjasejvyllaylswnzhemgeuhhypdobfbnftrorrbctbnlxcmghbonvvxvmajqfmfmgwbzpebigqwfsioblergcoeoqp"
b= "gvclhkjkjarmjxchewruadzrlbhprxfaujlbtxocxfoiespkohfokehvhqnynuyhdmlwlbakgqtmiiwwrdndjubqlqrakrkndxlqynbedusleojyswbbteugulgecqtipeynrztuvlhacrywnbxggtmaevhjnardhpqarkxmxeozvovlqvtyoiyvdfeqgxvpoopfymuxrixoxuzpptngblbgthybguquifciuwhlgezfzbuqwhwxvzfqidrozjjjqntkjbxrfzxgarzwbxvyzaohfhyfsjqiwkvflswstvbtnarqzmqymeiungzhprrnbmsohqhaokwdmntlajmopuiecjltdcgeratascagmyjamelopzeetpkxavsdyykradrvhtbvsnvgtiujiapdpadqxvvvwfowkfrrzvotklzduvoexejngmfdiabegpcqxukwrarbmqginxokdxzjkeouhpanhcfeyrcrstugldoaacmdbmonschzujodmwhmnlehgantdbtdffghtwumbelvnaybwhqlswtawgtaiodptmypitbjzmgoogqkniwherhaxaahqexmsvbcqcopougfbwpqgnykefkeillarkmlinnypbqgywlzucpaspkwxwchjohaaunihbjzebfczqdtuvvmkhlhfnopdwresfozgxykafnzxsusnreyapfgdwvguommtbnbammbtbcrtxjhqnhrdoxikuoeidscegdgurjnumeqlnzddguiutqhngnyjgapofyizhvtvclirkmuqgcnasupbhnkppcdvalwjjrfldpcnbzgkbvmwpbxypjogltdnhzzqrgdwvhlxgrjkmvidwfenqsucnxruzqmqwpmuzxrhratfxbltgpjxjdbwcutbnftlxhfyhyfaybfxcsrljckshnrjhknwrgioqnoxmuxmxekzzdkifwbmjuxrgknztxojlegzaflxjxxiajthgwtpqriydyxwvnfisnhsuvqespovyjcgfyyvrgvugttcgamaowtirlolafiaolhulfrcnnyuiryoskpigkqzvhnxovzeggatnsvdhuxplxffjwnsigrfnecdachikieaczdlvcchzhokgccoiuuxawacajnnrrpvquioykxzsljynmovgisihuljeawxrntjhbxfmueggogtauridlsmgdvkduhwhcgpedwsadagribtcsdhevtkbpugjddsglhmoggojgwcoyxsscawxviamehximqoxzcnfieqqasearyttaptwytkeckmqacnbedjmhzcjuikljdfjuahutszycloeqehuhqjosnzoyjbhmiqhiybcsccwoqcgujabclrwzrkzcngpwyyeybiqekmuboaxacbcouyplkoqxwftufatiilmvyiyokvopysdtsugckwcgbxcixxrijffjodxaaopziusboyfavhiyfljeiamtfrcvwcwxsnwaiqbwqjznqhoxuxcfzqygkbcgfadxnbxxtbukkvxacnyzkaejqcscfujkwohlshjlifxsaxueksdxujgnmyptuagsppghwpuewsywrtcbniykrhzfhqberhwiwcrvtlzpfanwvsaiaaurhvzrmavfhtnfwearrchxcwvxovhoweifzhwnhrsqlfvjlwcdalccixbwvkntqxyqexfnoydbfamrypwycyckvdjsqwlgvkyzheoxerbjtpcsgyqjwttuycmoayxvkxwtbkqhdtrxjtppshaqaukzyxpbvoyhmxaphsxnmqkxjbmdinuljemjdbkaqlheihtrasemiqlstxxcmrpxybhbcteuelamvuevokjxdurwtoaiipfiqolviprodsdyojvctebwastvjvdtllbdzoyjeqyhkbhykccfieciyxfjsjcfwfjvuhhazfjjiqhuukzcqdmoaryvccayijwetdeukneufnozzndptpgtgeqjgrjqcfuxkyswnyqungvnwyepnkkwobhxuqnyyiwiiqhyqxsdeqsaoxrchbyychxyxkxvuvgfnnddmxiqnbscalgjngjrngqmtniniqsxdxcpvkikncopowzbcksrrkekxozheuejrgaotkzinnydkzgojagclmoicosiiyrbftqaepitegwohefrentrzicdyulisejzxbzdqkwxsulaysrffmwgwyjwuwenaqoarqdkaahswusxnlcuyabwbmtvjxklpzlhpptrrajnwekjpoeprhmstfpeeaqubbdsqyjjyuxwyjiqaofrvtlqaavhcldfmgxfeioefnafzixzwfstydkbffiislngtnlzxcfcrhkqqhpomhknmuosbwatjpbcepdcrigipqbhaqymaizmengfliawybacqdgjnpudhvmhnkunsvcylkdytfvrhvvzzejotfraaeknqgdlbhjorpnkukdbfbdgfmvaroctumilsnyuwhkowxarjguphxxolsoehqzbfioxvmtsweisdklnqiexfbltubxduxgzhvwejsyfwgabrlqhvuhbwuwsytvssbtzyreijcnhlnjebznwuuzsrvkprfjjiclhtrrfvemguxkxxavtwxlnsxelenxmrivnzmsutgdpepmdphwoejbzgikmxhyprweskypdeuskjenbolpuusvcagoypppjntdxrsbxmviycxzsjqmfkiklqylhpcsevwcoofldavbctcucujhetrrjsesjglobjqrxvfcxafctjwxdhfkayblsgecorssaijzfoccpjgktdiwmpgnnkygsekgvcyxmkxrybvpkccfhkcvbkiowjwqnixlkxiyhfriinzvrdaanevqrgfnpdeemdpycaxmhowqdxlwbnyqswhjcoytrexfjpgmpfywtuozrbxupwlhusswiqrzxohgfnswustpojoglocaknjehbcprtrqjaxrppnjkiyysngddjfpyovgpxxisqzdqwufnioxsnwkccpfnuumipszoriiijlyhiewquukjsvlwkskfoypfsptjzdrkpsrxynpujzedwpchkmoymfeewznvdhhubyrzoitxjzdgpfpztdzfkdjhfyeihmcikvjaffaoeduvklwdqwkbbvigtmqbyullpvlwclliqheatafjypmakuiejzhhvuunrgjttwcmeimziskjhxjuttycuhmqbgdtomoklqwpakqjccumzfgvygxtpljssoliccsnuoevzugdxaryfxvdftywejpyxchaezpzquurocuncmohljmtelplugjujsunujokfkbumxjolzxzjmspxjatqmnzgjoavdkapnwcngqyhqxqcribbiutwiudtidonqpdflfutxtbpstrmbspmpiizcnsmrhajyfqlklhjgkzyfqmjlbvalfbpvtcocexcjnotyxeehdfowtxhxujickaxfcligkkrzakyxqegulvqfuzcrkmtumszqdjypwpowbowstemgbelwfpnpeijsakldwjssbiocxmwqriysokotbdihltalgnqcwkuztkcqzyiqjgixsztweddqxfdfswhrgdqbputovbeekpdeqyaucgmbnqggmpzusrwjmpajtepfvsjltmgvsuwfkenytovniryuiyfdduiamumhgucaoahbexbzlwmtplpyjwboqmrfgdmmzroprvqyssxgqmbgztekphzgtslbvzpwqdlizeitwfbmtdssyyfnievdyiftiuryycizgqueywttbnozmtmwzkzxsgscbjbbnlcwewaestxtjluxehtftsclzuocdrdtehpkdpoylorubmrivmnqgqbhkrjqkolrvabbrqzcgsyhgrpdddtktvrfobxbrispktqclpgrhfbqwqtatnmokdwygvbygvpqrfucwbwfgxveppelcqzowxmctqcblrtcyohupdaxcxbtmieqaeewdtbylfzwztzxjguylwvptyiignahtfdyagxlmwjlriiaqeadaxuwwfecuejplpnnvkahjksauddnhdskbngxukboqndecqtzdujmgdoagrnqxgaavizpuadmpiqramtdicrofgoozegymiyhqzykcdwrlpjnberjgkzlqpbsthqhprofqorsrqkefvsizlthvuuojwgddykvrbcipwcjmontlfdkqyrosocbkkgpktkcwpmllquxfkqqpvditwwlkamwmtmyoyaknoxyfuvmenetihddgbosddppybomzqwnhtnonlaraenlosowudoxgdpegfsgvovejisztsquzfhpavluyztgfimlnetluqpezifucxqddxsdvdztfucmfozuvthrjxxkhchlazpfzhkunjpsfrekidffymwkluwuydgyfvdeenarypjghpqrvxwvmufzoeunhanoxtubguthkentufkrfimrcuqtymihovwloqpxliexotqkacbfkqymmrfkdntslpfziuyvceurxkbamffyvgmhxstahmuueauousjzxfswpvwdaedxmpgjjbltognuihicctdbyvzprwutcxtoozzydkrrsenaovfsqitqesfxqbsuylkmnjmqwdjokwpytuqjelzifghwhashldvymiqinzzxvoxokpzoaazggiepiwywzuwoenytoxtknqaziaqiarqjzwaktziuvekbtluiipuyiuzqwpaxitiipiukhcfeirfeccmnrinzcmpbesymliwaqqlassedjmhoovbfdqhheyiiqixdqtehmrjejnhuzokplnxodewiegsvppafleoxxxdglldmbpcndzdifbqjijgxahelntilsmtfzyscowrrxxzcysngdufddkrqfzbxnxfovxrjvkcshcugwjozducigvznvcmkzrzxqqilcldkpzsljgmoaqximyvhcktebsbskjfnwjxlkpyvxkmyblipjgwnqprtksnuethaegooxomvzyvcldrulpjdgbxqvknzduchdsyagkvfksjxyctjrcnadkqzwdaaacjfujfdtdkfvucvwvfqysqdeiccodeohotcxaftfradlfykadaaxsedaigolketaxxyaetfvtijahtbmvdknjppsvefiiykixikbdpzzaizhbcvyghlrxcjugrerppznzjqdapeaxdjagfyoolhlotgwkmnbboobzheawkcwnoyvvxljktvamdxwpmxrbouaxacvkfrxvqvqpgzbzwenzdlrplkqbetygxtqenpzfkpwrpzsndipgtgwesohyjfehbwlqlnvyctptsjhwrwenearyrzyagcjhaxzlkujopaiikrgdpkqvnktelrgrvqbvpaizxunmuxwgqcmfnccamvgzomrleuiturutlkihheoyhafweiytfeswslhzfqucjpvwbddiitirtqpayntftlbnzlmedjgmaekbjnjthukckbckoxrjltxkglqjuxxudhvmwhidduipwmbkmsuxltjtezczwzvbitqfaykdsuuohvbtnxsbqbuuaxvzytajmqomqarlvnzeicxvzryrstmssjtscubomrcfsvqpirtsusovjmnbhbvzkpsnlvdxniehduwomrggjwdslqtsrouefotqjwqyguhmrfadwilffoxshskyjeeouxhguxectooktonqzavervyyniywpdnjaurwrwzmknxfemvdntjgohebrcaifnuihleahdmttlbxawcprlvfuzjlblujyorhzxhjbvewjhtjevyxitdcsopvzjgxzxgbvpmyksuvapegmcduxiypwnnvztuatcdqrpqekmzkbesnivjgejxcwmyxguybxbtotjsdvupyyhnieyoiholdaldihbjgecxxnrcilrilavuftipaycgznjhxmrfqvcqjuuthmctoznttxlvwnbxdkeayxfpvkhgebznpdgedvzwtktryvqbhudgukxpuevahwozcuffsedlrwertuubqxhkjgbemygtxuuzrzgjejwxhcobwicohlbsrcwfdfycbvbsuhdasbxzdncbxeqerrxkvvpacqcelfyfocggdfijvkksrczivytrvktyaycldatsebakiitdtfwkivudtnwqyqoaqsmtthnziojqwcwrisdspyvknsankpoahcvcjjctxnlvshnabquqqpaejbrvsfxzjteseindvzyninpkgjcwbfckguiabfblaffgntjjukwexoqfxteyyglgctgeahrbnwhcrtnldkscaikxdoybujjzerdezuhoqrskkgxpqptsydpdtnhqyqpcisjjoszgjrqvxompdghdlxhfmovngkpqeazstyyeqpcnfodiwkoijxpwlkjtwakadjswkscahgpovsztfndoksmxevqaycabmuzyndywknlhikanxgdjyqifnyfldiopcpnptnmdcxkkhmzgsdrttzagxfuanirqygftvtwyqikzwkfrnwmivmovtkxjtrztzgmvakvsufssrzjgyxovlfsfpsokjpdkvrhxdcsxkmqbnbinbyjmddrvvffgultscaridjfnxxqlbayczjqcnixkpdtmqmgumxcrjkgijxtkxuowdfbspafedyqvmyqyyssjcyrmxlyvfptkuudjvkpaiiywgowegonlnfzmsxhzmdlizqtwajxirvgzldgtrvegcdtudcvpfhafxtbycaivxpxisdclyisbmnxrptixciczcfzgikefbbqvgugecahqnfhfaqceygfcnflvrpbsstnynvepwmiltpqvhuziaekolxlcomwghjeuhlmdzuoslhptbobeunuglfkbujibuowbzkeyevspchkdvnjsbdaojkpdtzgoocppowosriktqwynkifnlfbwssznsgdikvxbrnviwfdmedzolhbzoevgyxuqfzapuyqllovhvavzexnpeqoswmbvjxnowofrmyezmcjhcehgdwyhpoclafgjcuzakftydaxpcgwgnfnqenatdegejnpnjpptultzlqopzmvoukgyxgtbmzhvowkzncujnniyeynfnkthvzhuiavubesqdcpqekarxkrdjgiyrdfmfognoehpizhlexekjgeiqvobewzvcghhupuitdaefjpjivvrbzcsxqtbovwqbfzwuvgqzgweqlpyjkskmucjmykatitunsqjoxbpfxvxlkyuwqekmjtyhfacntwcopmeoptvnqtyarsyjyjvhevomvszrrchgqnwfituymuafoaqnlnuqilcgddzuhiczvahfubdiwfqkfgzruujehnmmsljavnzsoixkkcsihksprsgnorrxgglytuypkajaihkulecvpxkirsvhlogrurpqmqfysoycxixlobgfaqntkkavbimxadnotumllkqiupvkqbqttfmdspytxmszqgnjazxnlnyfctquviponcuftuashtsxzhibhfpsunayiqtdakunoovhivcrowopdxrmeifbxhzfzulzffmtvjdffhxtdljikcvrkcujjvoiszjxexsbhxhmgeflrquesrvevpngmeqedzdkwyldvspcyxpqpjukcrqxiefuivznucztalwyfocgnrwcdsofjfftlknvgoictivtvutckxixpgbuyszjxgcitqdzgndzvbvsvovhmdedkhxkzyuyhwgaolbvzeuuhpncgklunpxzzwkywgzdefdtrgqqnmmuebzklkgbcdcbbmbxuadziiuzpmrcyfycjxowiuxkzancooclrfkzngaestisahxjelgoifajhnmyeojxtvwidynxrvptcmdjalxksytanfarvloqgmzlmoidlxzqmczmpywhyrjmzjfuwwlckmnxavclvbdhdevudtebknpjzvevtpaddpadndqieurkymgdfkfrawbztfwmwyqzosedvuncqeorsuuzfbqhyrgryegwdwxrobwmyjoqpehhycgffymfsuxqzdpcbmvrqrdqctgrxoyysgdxgsdyocrnhgrkuobkhfajyjawxaurizqptvnizgxgmpqhfstnzwyxfbvedpvmrndkjssizqrnhhwobqbcmcatfvxinuwghbqqulzvdqkkzhydxcflghelfdvuxuaevsvrdwoiozupgtsfxaqfhwsozniwjkcfdxyivnrjmlzugtzfvrkdnetoscmdmoirojalwrxkcwelrfqnwdslhlzbpnfcdpttyvfumcgrakctrugnxayfmzidmnhsdblbysylugewtiqkcyyczyjnyrqmfygkbsnzknmhuqdnatxdsxftwqgwhykowryzlmzvznetgiigdglxdsqbiyxqxietbdvmrujsjoopywydejbictlksjcpthkumfifbrxlhnchkalomoyqhkcbvfqqodkciuhmlgzvubcgepwsdxinjkoephwfkghucqgnzhkvjpbpezhkwrzhbnntwjygpidrajhzrtucixtpxcbvtadwnqpkaqsravlahuaynwcyuxntzoqsotodmgpmyifyfqymmamazqavnnomdggtaxwmdoabwhbdabqmceodvoyidoxgudzwawkfkmiiulnunfirkxuhnuprioxesxbuvlchymruyeqlkycwxydlsucajzedyhzvtdctqtpoafbmffiddlovfsxqrbtsjvneyqzoloenvfzakjdnwtkelhuflqxwlmajebysrefmkhmwqsmnlwrzgnerddnoppauqamjetvqajntbbipzbofouwuxjkoakkqmyzrswjugynjzxazyqgpkdjjotapgkhsjjldfvxntnzvkzulqaaafjmwemlmyufhdsmlnmyjzxelzawpcyrijfeorraqlhzpaoapaaybacozcnqfljpvptliklavvcmxqomqpltpnhqsuixirmdihortbroytdvlribgtwxienaavziplnxsdolhicfdhbpylshgpgovwrvtqgictgwzwkggolmvobvbvehklyhhpfaflljgtifpulykzkhpncrijyvuwednjdvwoedjokbiwzsxlbmyedipefjckmqtrlsirvrgfsqdtlaempessphyusbggrayesivpbdwuwcpheuttaoopvmmonsuguumoekdgncajepskloeocudzgpnwikecgtrldwrsatcekupyivmmrpmxhbvrlcvuvmfalwslrwsbrjzbglqxdcwkdsdrwyltnqtyonlfkdidmiesvwpyymkegnvemgzzyuzohkvrqducnbxjxojwcuckjxqvfpwfjvtriokytfchgbqdqzbuvdhfcxcjnzoywjrgxcethhapiquarwvnbesgbwpqxepupgcnkhgrqigyybbrzyeccykdvauuglovttkeasxqaeqahrsirymtxxzuztohgfezypfajdqmjimscgctfqpepoaojqxpvcqvtyvcbnomydeclivsymwoaycjpcamerkxrhzsxqevvkxgsuzqhxejwjtnnvbroloftpxqhdncpmjhikarhgbfrwuerwvgjllcdjukojpexyngknxtuabnwvsotpuddhhiseshpjnnjattosnkvqzrlthhjdmolvwdzqmrazejazfqtscokbgvvnegrqwcoshpkugmtkytjdldxnrhpzemplsgdokrithunnhhafcjkqohdiqujwgyhygloqcwmjtzzaizhnkrdbaglsbuojtwkbhyujxgvqfwsoxzdhsgksovkrsyblwlodlipkomcuiukfvnonvzhjwtbouebqrqucylpnxrjfovmjiczddgoaapquvsmmkgritgxqzixndlznoyqrghtiykeuergozxytdwjfejskutxirqcaxvivhnpleyzdvyybwiicramnukyn"
print(number_needed(a,b))