// Generated from C:/Users/Patryk/Documents/Studia/Semestr 4/Kompilatory/Transpiler\VyperLexer.g4 by ANTLR 4.12.0

from antlr_denter.DenterHelper import DenterHelper
from dist.VyperParser import VyperParser

import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class VyperLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.12.0", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		INDENT=1, DEDENT=2, AS=3, FROM=4, IMPORT=5, DOT=6, COMMA=7, COLON=8, ASSIGN=9, 
		AT=10, LPAREN=11, RPAREN=12, LSQUARE=13, RSQUARE=14, LCURLY=15, RCURLY=16, 
		CONSTANT=17, IMMUTABLE=18, PUBLIC=19, INDEXED=20, DYNARRAY=21, FUNCDECL=22, 
		RETURNTYPE=23, EVENTDECL=24, ENUMDECL=25, MAP=26, STRUCTDECL=27, INTERFACEDECL=28, 
		SKIPASSIGN=29, ADD=30, SUB=31, MUL=32, DIV=33, MOD=34, POW=35, SHL=36, 
		SHR=37, PASS=38, Break=39, CONTINUE=40, LOG=41, RETURN=42, RAISE=43, ASSERT=44, 
		IF=45, ELSE=46, ELIF=47, UNREACHABLE=48, FOR=49, IN=50, AND=51, OR=52, 
		NOT=53, NEG=54, BITAND=55, BITOR=56, BITXOR=57, EQ=58, NE=59, LE=60, GE=61, 
		LT=62, GT=63, EMPTY=64, ABIDECODE=65, BOOL=66, NAME=67, TYPE=68, STRING=69, 
		DOCSTRING=70, DECNUMBER=71, HEXNUMBER=72, OCTNUMBER=73, BINNUMBER=74, 
		FLOATNUMBER=75, SPACES=76, NEWLINE=77, COMMENT=78;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"AS", "FROM", "IMPORT", "DOT", "COMMA", "COLON", "ASSIGN", "AT", "LPAREN", 
			"RPAREN", "LSQUARE", "RSQUARE", "LCURLY", "RCURLY", "CONSTANT", "IMMUTABLE", 
			"PUBLIC", "INDEXED", "DYNARRAY", "FUNCDECL", "RETURNTYPE", "EVENTDECL", 
			"ENUMDECL", "MAP", "STRUCTDECL", "INTERFACEDECL", "SKIPASSIGN", "ADD", 
			"SUB", "MUL", "DIV", "MOD", "POW", "SHL", "SHR", "PASS", "Break", "CONTINUE", 
			"LOG", "RETURN", "RAISE", "ASSERT", "IF", "ELSE", "ELIF", "UNREACHABLE", 
			"FOR", "IN", "AND", "OR", "NOT", "NEG", "BITAND", "BITOR", "BITXOR", 
			"EQ", "NE", "LE", "GE", "LT", "GT", "EMPTY", "ABIDECODE", "BOOL", "NAME", 
			"TYPE", "STRING", "DOCSTRING", "ESC", "DECNUMBER", "HEXNUMBER", "OCTNUMBER", 
			"BINNUMBER", "FLOATNUMBER", "SPACES", "NEWLINE", "COMMENT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, "'as'", "'from'", "'import'", "'.'", "','", "':'", 
			"'='", "'@'", "'('", "')'", "'['", "']'", "'{'", "'}'", "'constant'", 
			"'immutable'", "'public'", "'indexed'", "'DynArray'", "'def'", "'->'", 
			"'event'", "'enum'", "'HashMap'", "'struct'", "'interface'", "'_'", "'+'", 
			"'-'", "'*'", "'/'", "'%'", "'**'", "'<<'", "'>>'", "'pass'", "'break'", 
			"'continue'", "'log'", "'return'", "'raise'", "'assert'", "'if'", "'else'", 
			"'elif'", "'UNREACHABLE'", "'for'", "'in'", "'and'", "'or'", "'not'", 
			"'~'", "'&'", "'|'", "'^'", "'=='", "'!='", "'<='", "'>='", "'<'", "'>'", 
			"'empty'", "'_abi_decode'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "INDENT", "DEDENT", "AS", "FROM", "IMPORT", "DOT", "COMMA", "COLON", 
			"ASSIGN", "AT", "LPAREN", "RPAREN", "LSQUARE", "RSQUARE", "LCURLY", "RCURLY", 
			"CONSTANT", "IMMUTABLE", "PUBLIC", "INDEXED", "DYNARRAY", "FUNCDECL", 
			"RETURNTYPE", "EVENTDECL", "ENUMDECL", "MAP", "STRUCTDECL", "INTERFACEDECL", 
			"SKIPASSIGN", "ADD", "SUB", "MUL", "DIV", "MOD", "POW", "SHL", "SHR", 
			"PASS", "Break", "CONTINUE", "LOG", "RETURN", "RAISE", "ASSERT", "IF", 
			"ELSE", "ELIF", "UNREACHABLE", "FOR", "IN", "AND", "OR", "NOT", "NEG", 
			"BITAND", "BITOR", "BITXOR", "EQ", "NE", "LE", "GE", "LT", "GT", "EMPTY", 
			"ABIDECODE", "BOOL", "NAME", "TYPE", "STRING", "DOCSTRING", "DECNUMBER", 
			"HEXNUMBER", "OCTNUMBER", "BINNUMBER", "FLOATNUMBER", "SPACES", "NEWLINE", 
			"COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	ignore = False
	bracketCount = 0

	def openBracket(self):
	    self.bracketCount += 1
	    VyperLexer.ignore=True

	def closeBracket(self):
	    self.bracketCount -= 1
	    if self.bracketCount == 0:
	        VyperLexer.ignore=False

	class MyCoolDenter(DenterHelper):
	    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
	        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
	        self.lexer: VyperLexer = lexer

	    def pull_token(self):
	        return super(VyperLexer, self.lexer).nextToken()

	denter = None

	def nextToken(self):
	    if not self.denter:
	        self.denter = self.MyCoolDenter(self, self.NEWLINE, VyperParser.INDENT, VyperParser.DEDENT, False)
	    return self.denter.next_token()


	public VyperLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "VyperLexer.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	@Override
	public void action(RuleContext _localctx, int ruleIndex, int actionIndex) {
		switch (ruleIndex) {
		case 8:
			LPAREN_action((RuleContext)_localctx, actionIndex);
			break;
		case 9:
			RPAREN_action((RuleContext)_localctx, actionIndex);
			break;
		case 10:
			LSQUARE_action((RuleContext)_localctx, actionIndex);
			break;
		case 11:
			RSQUARE_action((RuleContext)_localctx, actionIndex);
			break;
		case 12:
			LCURLY_action((RuleContext)_localctx, actionIndex);
			break;
		case 13:
			RCURLY_action((RuleContext)_localctx, actionIndex);
			break;
		case 75:
			NEWLINE_action((RuleContext)_localctx, actionIndex);
			break;
		}
	}
	private void LPAREN_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 0:
			self.openBracket()
			break;
		}
	}
	private void RPAREN_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 1:
			self.closeBracket()
			break;
		}
	}
	private void LSQUARE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 2:
			self.openBracket()
			break;
		}
	}
	private void RSQUARE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 3:
			self.closeBracket()
			break;
		}
	}
	private void LCURLY_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 4:
			self.openBracket()
			break;
		}
	}
	private void RCURLY_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 5:
			self.closeBracket()
			break;
		}
	}
	private void NEWLINE_action(RuleContext _localctx, int actionIndex) {
		switch (actionIndex) {
		case 6:

			    if VyperLexer.ignore:
			        self.skip()

			break;
		}
	}

	public static final String _serializedATN =
		"\u0004\u0000N\u0256\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002"+
		"\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002"+
		"\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002"+
		"\u001b\u0007\u001b\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002"+
		"\u001e\u0007\u001e\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007"+
		"!\u0002\"\u0007\"\u0002#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007"+
		"&\u0002\'\u0007\'\u0002(\u0007(\u0002)\u0007)\u0002*\u0007*\u0002+\u0007"+
		"+\u0002,\u0007,\u0002-\u0007-\u0002.\u0007.\u0002/\u0007/\u00020\u0007"+
		"0\u00021\u00071\u00022\u00072\u00023\u00073\u00024\u00074\u00025\u0007"+
		"5\u00026\u00076\u00027\u00077\u00028\u00078\u00029\u00079\u0002:\u0007"+
		":\u0002;\u0007;\u0002<\u0007<\u0002=\u0007=\u0002>\u0007>\u0002?\u0007"+
		"?\u0002@\u0007@\u0002A\u0007A\u0002B\u0007B\u0002C\u0007C\u0002D\u0007"+
		"D\u0002E\u0007E\u0002F\u0007F\u0002G\u0007G\u0002H\u0007H\u0002I\u0007"+
		"I\u0002J\u0007J\u0002K\u0007K\u0002L\u0007L\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b"+
		"\u0001\b\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001"+
		"\u0012\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001"+
		"\u0014\u0001\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001\u0017\u0001"+
		"\u0017\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001b\u0001\u001b\u0001"+
		"\u001c\u0001\u001c\u0001\u001d\u0001\u001d\u0001\u001e\u0001\u001e\u0001"+
		"\u001f\u0001\u001f\u0001 \u0001 \u0001 \u0001!\u0001!\u0001!\u0001\"\u0001"+
		"\"\u0001\"\u0001#\u0001#\u0001#\u0001#\u0001#\u0001$\u0001$\u0001$\u0001"+
		"$\u0001$\u0001$\u0001%\u0001%\u0001%\u0001%\u0001%\u0001%\u0001%\u0001"+
		"%\u0001%\u0001&\u0001&\u0001&\u0001&\u0001\'\u0001\'\u0001\'\u0001\'\u0001"+
		"\'\u0001\'\u0001\'\u0001(\u0001(\u0001(\u0001(\u0001(\u0001(\u0001)\u0001"+
		")\u0001)\u0001)\u0001)\u0001)\u0001)\u0001*\u0001*\u0001*\u0001+\u0001"+
		"+\u0001+\u0001+\u0001+\u0001,\u0001,\u0001,\u0001,\u0001,\u0001-\u0001"+
		"-\u0001-\u0001-\u0001-\u0001-\u0001-\u0001-\u0001-\u0001-\u0001-\u0001"+
		"-\u0001.\u0001.\u0001.\u0001.\u0001/\u0001/\u0001/\u00010\u00010\u0001"+
		"0\u00010\u00011\u00011\u00011\u00012\u00012\u00012\u00012\u00013\u0001"+
		"3\u00014\u00014\u00015\u00015\u00016\u00016\u00017\u00017\u00017\u0001"+
		"8\u00018\u00018\u00019\u00019\u00019\u0001:\u0001:\u0001:\u0001;\u0001"+
		";\u0001<\u0001<\u0001=\u0001=\u0001=\u0001=\u0001=\u0001=\u0001>\u0001"+
		">\u0001>\u0001>\u0001>\u0001>\u0001>\u0001>\u0001>\u0001>\u0001>\u0001"+
		">\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0001?\u0003"+
		"?\u01bc\b?\u0001@\u0001@\u0005@\u01c0\b@\n@\f@\u01c3\t@\u0001A\u0001A"+
		"\u0005A\u01c7\bA\nA\fA\u01ca\tA\u0001B\u0003B\u01cd\bB\u0001B\u0001B\u0001"+
		"B\u0005B\u01d2\bB\nB\fB\u01d5\tB\u0001B\u0001B\u0003B\u01d9\bB\u0001B"+
		"\u0001B\u0001B\u0005B\u01de\bB\nB\fB\u01e1\tB\u0001B\u0003B\u01e4\bB\u0001"+
		"C\u0001C\u0001C\u0001C\u0001C\u0001C\u0005C\u01ec\bC\nC\fC\u01ef\tC\u0001"+
		"C\u0001C\u0001C\u0001C\u0001C\u0001C\u0001C\u0001C\u0001C\u0005C\u01fa"+
		"\bC\nC\fC\u01fd\tC\u0001C\u0001C\u0001C\u0003C\u0202\bC\u0001D\u0001D"+
		"\u0001D\u0001D\u0001D\u0001D\u0003D\u020a\bD\u0001E\u0004E\u020d\bE\u000b"+
		"E\fE\u020e\u0001F\u0001F\u0001F\u0001F\u0005F\u0215\bF\nF\fF\u0218\tF"+
		"\u0001G\u0001G\u0001G\u0001G\u0005G\u021e\bG\nG\fG\u0221\tG\u0001H\u0001"+
		"H\u0001H\u0001H\u0005H\u0227\bH\nH\fH\u022a\tH\u0001I\u0003I\u022d\bI"+
		"\u0001I\u0005I\u0230\bI\nI\fI\u0233\tI\u0001I\u0003I\u0236\bI\u0001I\u0004"+
		"I\u0239\bI\u000bI\fI\u023a\u0001J\u0004J\u023e\bJ\u000bJ\fJ\u023f\u0001"+
		"J\u0001J\u0001K\u0003K\u0245\bK\u0001K\u0001K\u0005K\u0249\bK\nK\fK\u024c"+
		"\tK\u0001K\u0001K\u0001L\u0001L\u0005L\u0252\bL\nL\fL\u0255\tL\u0004\u01d3"+
		"\u01df\u01ed\u01fb\u0000M\u0001\u0003\u0003\u0004\u0005\u0005\u0007\u0006"+
		"\t\u0007\u000b\b\r\t\u000f\n\u0011\u000b\u0013\f\u0015\r\u0017\u000e\u0019"+
		"\u000f\u001b\u0010\u001d\u0011\u001f\u0012!\u0013#\u0014%\u0015\'\u0016"+
		")\u0017+\u0018-\u0019/\u001a1\u001b3\u001c5\u001d7\u001e9\u001f; =!?\""+
		"A#C$E%G&I\'K(M)O*Q+S,U-W.Y/[0]1_2a3c4e5g6i7k8m9o:q;s<u=w>y?{@}A\u007f"+
		"B\u0081C\u0083D\u0085E\u0087F\u0089\u0000\u008bG\u008dH\u008fI\u0091J"+
		"\u0093K\u0095L\u0097M\u0099N\u0001\u0000\t\u0003\u0000AZ__az\u0004\u0000"+
		"09AZ__az\u0001\u000009\u0002\u000009af\u0001\u000007\u0001\u000001\u0002"+
		"\u0000++--\u0001\u0000..\u0002\u0000\n\n\f\r\u0271\u0000\u0001\u0001\u0000"+
		"\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000"+
		"\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000"+
		"\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000"+
		"\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000"+
		"\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000"+
		"\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000"+
		"\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000"+
		"\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000"+
		"#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001"+
		"\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001\u0000\u0000"+
		"\u0000\u0000-\u0001\u0000\u0000\u0000\u0000/\u0001\u0000\u0000\u0000\u0000"+
		"1\u0001\u0000\u0000\u0000\u00003\u0001\u0000\u0000\u0000\u00005\u0001"+
		"\u0000\u0000\u0000\u00007\u0001\u0000\u0000\u0000\u00009\u0001\u0000\u0000"+
		"\u0000\u0000;\u0001\u0000\u0000\u0000\u0000=\u0001\u0000\u0000\u0000\u0000"+
		"?\u0001\u0000\u0000\u0000\u0000A\u0001\u0000\u0000\u0000\u0000C\u0001"+
		"\u0000\u0000\u0000\u0000E\u0001\u0000\u0000\u0000\u0000G\u0001\u0000\u0000"+
		"\u0000\u0000I\u0001\u0000\u0000\u0000\u0000K\u0001\u0000\u0000\u0000\u0000"+
		"M\u0001\u0000\u0000\u0000\u0000O\u0001\u0000\u0000\u0000\u0000Q\u0001"+
		"\u0000\u0000\u0000\u0000S\u0001\u0000\u0000\u0000\u0000U\u0001\u0000\u0000"+
		"\u0000\u0000W\u0001\u0000\u0000\u0000\u0000Y\u0001\u0000\u0000\u0000\u0000"+
		"[\u0001\u0000\u0000\u0000\u0000]\u0001\u0000\u0000\u0000\u0000_\u0001"+
		"\u0000\u0000\u0000\u0000a\u0001\u0000\u0000\u0000\u0000c\u0001\u0000\u0000"+
		"\u0000\u0000e\u0001\u0000\u0000\u0000\u0000g\u0001\u0000\u0000\u0000\u0000"+
		"i\u0001\u0000\u0000\u0000\u0000k\u0001\u0000\u0000\u0000\u0000m\u0001"+
		"\u0000\u0000\u0000\u0000o\u0001\u0000\u0000\u0000\u0000q\u0001\u0000\u0000"+
		"\u0000\u0000s\u0001\u0000\u0000\u0000\u0000u\u0001\u0000\u0000\u0000\u0000"+
		"w\u0001\u0000\u0000\u0000\u0000y\u0001\u0000\u0000\u0000\u0000{\u0001"+
		"\u0000\u0000\u0000\u0000}\u0001\u0000\u0000\u0000\u0000\u007f\u0001\u0000"+
		"\u0000\u0000\u0000\u0081\u0001\u0000\u0000\u0000\u0000\u0083\u0001\u0000"+
		"\u0000\u0000\u0000\u0085\u0001\u0000\u0000\u0000\u0000\u0087\u0001\u0000"+
		"\u0000\u0000\u0000\u008b\u0001\u0000\u0000\u0000\u0000\u008d\u0001\u0000"+
		"\u0000\u0000\u0000\u008f\u0001\u0000\u0000\u0000\u0000\u0091\u0001\u0000"+
		"\u0000\u0000\u0000\u0093\u0001\u0000\u0000\u0000\u0000\u0095\u0001\u0000"+
		"\u0000\u0000\u0000\u0097\u0001\u0000\u0000\u0000\u0000\u0099\u0001\u0000"+
		"\u0000\u0000\u0001\u009b\u0001\u0000\u0000\u0000\u0003\u009e\u0001\u0000"+
		"\u0000\u0000\u0005\u00a3\u0001\u0000\u0000\u0000\u0007\u00aa\u0001\u0000"+
		"\u0000\u0000\t\u00ac\u0001\u0000\u0000\u0000\u000b\u00ae\u0001\u0000\u0000"+
		"\u0000\r\u00b0\u0001\u0000\u0000\u0000\u000f\u00b2\u0001\u0000\u0000\u0000"+
		"\u0011\u00b4\u0001\u0000\u0000\u0000\u0013\u00b7\u0001\u0000\u0000\u0000"+
		"\u0015\u00ba\u0001\u0000\u0000\u0000\u0017\u00bd\u0001\u0000\u0000\u0000"+
		"\u0019\u00c0\u0001\u0000\u0000\u0000\u001b\u00c3\u0001\u0000\u0000\u0000"+
		"\u001d\u00c6\u0001\u0000\u0000\u0000\u001f\u00cf\u0001\u0000\u0000\u0000"+
		"!\u00d9\u0001\u0000\u0000\u0000#\u00e0\u0001\u0000\u0000\u0000%\u00e8"+
		"\u0001\u0000\u0000\u0000\'\u00f1\u0001\u0000\u0000\u0000)\u00f5\u0001"+
		"\u0000\u0000\u0000+\u00f8\u0001\u0000\u0000\u0000-\u00fe\u0001\u0000\u0000"+
		"\u0000/\u0103\u0001\u0000\u0000\u00001\u010b\u0001\u0000\u0000\u00003"+
		"\u0112\u0001\u0000\u0000\u00005\u011c\u0001\u0000\u0000\u00007\u011e\u0001"+
		"\u0000\u0000\u00009\u0120\u0001\u0000\u0000\u0000;\u0122\u0001\u0000\u0000"+
		"\u0000=\u0124\u0001\u0000\u0000\u0000?\u0126\u0001\u0000\u0000\u0000A"+
		"\u0128\u0001\u0000\u0000\u0000C\u012b\u0001\u0000\u0000\u0000E\u012e\u0001"+
		"\u0000\u0000\u0000G\u0131\u0001\u0000\u0000\u0000I\u0136\u0001\u0000\u0000"+
		"\u0000K\u013c\u0001\u0000\u0000\u0000M\u0145\u0001\u0000\u0000\u0000O"+
		"\u0149\u0001\u0000\u0000\u0000Q\u0150\u0001\u0000\u0000\u0000S\u0156\u0001"+
		"\u0000\u0000\u0000U\u015d\u0001\u0000\u0000\u0000W\u0160\u0001\u0000\u0000"+
		"\u0000Y\u0165\u0001\u0000\u0000\u0000[\u016a\u0001\u0000\u0000\u0000]"+
		"\u0176\u0001\u0000\u0000\u0000_\u017a\u0001\u0000\u0000\u0000a\u017d\u0001"+
		"\u0000\u0000\u0000c\u0181\u0001\u0000\u0000\u0000e\u0184\u0001\u0000\u0000"+
		"\u0000g\u0188\u0001\u0000\u0000\u0000i\u018a\u0001\u0000\u0000\u0000k"+
		"\u018c\u0001\u0000\u0000\u0000m\u018e\u0001\u0000\u0000\u0000o\u0190\u0001"+
		"\u0000\u0000\u0000q\u0193\u0001\u0000\u0000\u0000s\u0196\u0001\u0000\u0000"+
		"\u0000u\u0199\u0001\u0000\u0000\u0000w\u019c\u0001\u0000\u0000\u0000y"+
		"\u019e\u0001\u0000\u0000\u0000{\u01a0\u0001\u0000\u0000\u0000}\u01a6\u0001"+
		"\u0000\u0000\u0000\u007f\u01bb\u0001\u0000\u0000\u0000\u0081\u01bd\u0001"+
		"\u0000\u0000\u0000\u0083\u01c4\u0001\u0000\u0000\u0000\u0085\u01e3\u0001"+
		"\u0000\u0000\u0000\u0087\u0201\u0001\u0000\u0000\u0000\u0089\u0209\u0001"+
		"\u0000\u0000\u0000\u008b\u020c\u0001\u0000\u0000\u0000\u008d\u0210\u0001"+
		"\u0000\u0000\u0000\u008f\u0219\u0001\u0000\u0000\u0000\u0091\u0222\u0001"+
		"\u0000\u0000\u0000\u0093\u022c\u0001\u0000\u0000\u0000\u0095\u023d\u0001"+
		"\u0000\u0000\u0000\u0097\u0244\u0001\u0000\u0000\u0000\u0099\u024f\u0001"+
		"\u0000\u0000\u0000\u009b\u009c\u0005a\u0000\u0000\u009c\u009d\u0005s\u0000"+
		"\u0000\u009d\u0002\u0001\u0000\u0000\u0000\u009e\u009f\u0005f\u0000\u0000"+
		"\u009f\u00a0\u0005r\u0000\u0000\u00a0\u00a1\u0005o\u0000\u0000\u00a1\u00a2"+
		"\u0005m\u0000\u0000\u00a2\u0004\u0001\u0000\u0000\u0000\u00a3\u00a4\u0005"+
		"i\u0000\u0000\u00a4\u00a5\u0005m\u0000\u0000\u00a5\u00a6\u0005p\u0000"+
		"\u0000\u00a6\u00a7\u0005o\u0000\u0000\u00a7\u00a8\u0005r\u0000\u0000\u00a8"+
		"\u00a9\u0005t\u0000\u0000\u00a9\u0006\u0001\u0000\u0000\u0000\u00aa\u00ab"+
		"\u0005.\u0000\u0000\u00ab\b\u0001\u0000\u0000\u0000\u00ac\u00ad\u0005"+
		",\u0000\u0000\u00ad\n\u0001\u0000\u0000\u0000\u00ae\u00af\u0005:\u0000"+
		"\u0000\u00af\f\u0001\u0000\u0000\u0000\u00b0\u00b1\u0005=\u0000\u0000"+
		"\u00b1\u000e\u0001\u0000\u0000\u0000\u00b2\u00b3\u0005@\u0000\u0000\u00b3"+
		"\u0010\u0001\u0000\u0000\u0000\u00b4\u00b5\u0005(\u0000\u0000\u00b5\u00b6"+
		"\u0006\b\u0000\u0000\u00b6\u0012\u0001\u0000\u0000\u0000\u00b7\u00b8\u0005"+
		")\u0000\u0000\u00b8\u00b9\u0006\t\u0001\u0000\u00b9\u0014\u0001\u0000"+
		"\u0000\u0000\u00ba\u00bb\u0005[\u0000\u0000\u00bb\u00bc\u0006\n\u0002"+
		"\u0000\u00bc\u0016\u0001\u0000\u0000\u0000\u00bd\u00be\u0005]\u0000\u0000"+
		"\u00be\u00bf\u0006\u000b\u0003\u0000\u00bf\u0018\u0001\u0000\u0000\u0000"+
		"\u00c0\u00c1\u0005{\u0000\u0000\u00c1\u00c2\u0006\f\u0004\u0000\u00c2"+
		"\u001a\u0001\u0000\u0000\u0000\u00c3\u00c4\u0005}\u0000\u0000\u00c4\u00c5"+
		"\u0006\r\u0005\u0000\u00c5\u001c\u0001\u0000\u0000\u0000\u00c6\u00c7\u0005"+
		"c\u0000\u0000\u00c7\u00c8\u0005o\u0000\u0000\u00c8\u00c9\u0005n\u0000"+
		"\u0000\u00c9\u00ca\u0005s\u0000\u0000\u00ca\u00cb\u0005t\u0000\u0000\u00cb"+
		"\u00cc\u0005a\u0000\u0000\u00cc\u00cd\u0005n\u0000\u0000\u00cd\u00ce\u0005"+
		"t\u0000\u0000\u00ce\u001e\u0001\u0000\u0000\u0000\u00cf\u00d0\u0005i\u0000"+
		"\u0000\u00d0\u00d1\u0005m\u0000\u0000\u00d1\u00d2\u0005m\u0000\u0000\u00d2"+
		"\u00d3\u0005u\u0000\u0000\u00d3\u00d4\u0005t\u0000\u0000\u00d4\u00d5\u0005"+
		"a\u0000\u0000\u00d5\u00d6\u0005b\u0000\u0000\u00d6\u00d7\u0005l\u0000"+
		"\u0000\u00d7\u00d8\u0005e\u0000\u0000\u00d8 \u0001\u0000\u0000\u0000\u00d9"+
		"\u00da\u0005p\u0000\u0000\u00da\u00db\u0005u\u0000\u0000\u00db\u00dc\u0005"+
		"b\u0000\u0000\u00dc\u00dd\u0005l\u0000\u0000\u00dd\u00de\u0005i\u0000"+
		"\u0000\u00de\u00df\u0005c\u0000\u0000\u00df\"\u0001\u0000\u0000\u0000"+
		"\u00e0\u00e1\u0005i\u0000\u0000\u00e1\u00e2\u0005n\u0000\u0000\u00e2\u00e3"+
		"\u0005d\u0000\u0000\u00e3\u00e4\u0005e\u0000\u0000\u00e4\u00e5\u0005x"+
		"\u0000\u0000\u00e5\u00e6\u0005e\u0000\u0000\u00e6\u00e7\u0005d\u0000\u0000"+
		"\u00e7$\u0001\u0000\u0000\u0000\u00e8\u00e9\u0005D\u0000\u0000\u00e9\u00ea"+
		"\u0005y\u0000\u0000\u00ea\u00eb\u0005n\u0000\u0000\u00eb\u00ec\u0005A"+
		"\u0000\u0000\u00ec\u00ed\u0005r\u0000\u0000\u00ed\u00ee\u0005r\u0000\u0000"+
		"\u00ee\u00ef\u0005a\u0000\u0000\u00ef\u00f0\u0005y\u0000\u0000\u00f0&"+
		"\u0001\u0000\u0000\u0000\u00f1\u00f2\u0005d\u0000\u0000\u00f2\u00f3\u0005"+
		"e\u0000\u0000\u00f3\u00f4\u0005f\u0000\u0000\u00f4(\u0001\u0000\u0000"+
		"\u0000\u00f5\u00f6\u0005-\u0000\u0000\u00f6\u00f7\u0005>\u0000\u0000\u00f7"+
		"*\u0001\u0000\u0000\u0000\u00f8\u00f9\u0005e\u0000\u0000\u00f9\u00fa\u0005"+
		"v\u0000\u0000\u00fa\u00fb\u0005e\u0000\u0000\u00fb\u00fc\u0005n\u0000"+
		"\u0000\u00fc\u00fd\u0005t\u0000\u0000\u00fd,\u0001\u0000\u0000\u0000\u00fe"+
		"\u00ff\u0005e\u0000\u0000\u00ff\u0100\u0005n\u0000\u0000\u0100\u0101\u0005"+
		"u\u0000\u0000\u0101\u0102\u0005m\u0000\u0000\u0102.\u0001\u0000\u0000"+
		"\u0000\u0103\u0104\u0005H\u0000\u0000\u0104\u0105\u0005a\u0000\u0000\u0105"+
		"\u0106\u0005s\u0000\u0000\u0106\u0107\u0005h\u0000\u0000\u0107\u0108\u0005"+
		"M\u0000\u0000\u0108\u0109\u0005a\u0000\u0000\u0109\u010a\u0005p\u0000"+
		"\u0000\u010a0\u0001\u0000\u0000\u0000\u010b\u010c\u0005s\u0000\u0000\u010c"+
		"\u010d\u0005t\u0000\u0000\u010d\u010e\u0005r\u0000\u0000\u010e\u010f\u0005"+
		"u\u0000\u0000\u010f\u0110\u0005c\u0000\u0000\u0110\u0111\u0005t\u0000"+
		"\u0000\u01112\u0001\u0000\u0000\u0000\u0112\u0113\u0005i\u0000\u0000\u0113"+
		"\u0114\u0005n\u0000\u0000\u0114\u0115\u0005t\u0000\u0000\u0115\u0116\u0005"+
		"e\u0000\u0000\u0116\u0117\u0005r\u0000\u0000\u0117\u0118\u0005f\u0000"+
		"\u0000\u0118\u0119\u0005a\u0000\u0000\u0119\u011a\u0005c\u0000\u0000\u011a"+
		"\u011b\u0005e\u0000\u0000\u011b4\u0001\u0000\u0000\u0000\u011c\u011d\u0005"+
		"_\u0000\u0000\u011d6\u0001\u0000\u0000\u0000\u011e\u011f\u0005+\u0000"+
		"\u0000\u011f8\u0001\u0000\u0000\u0000\u0120\u0121\u0005-\u0000\u0000\u0121"+
		":\u0001\u0000\u0000\u0000\u0122\u0123\u0005*\u0000\u0000\u0123<\u0001"+
		"\u0000\u0000\u0000\u0124\u0125\u0005/\u0000\u0000\u0125>\u0001\u0000\u0000"+
		"\u0000\u0126\u0127\u0005%\u0000\u0000\u0127@\u0001\u0000\u0000\u0000\u0128"+
		"\u0129\u0005*\u0000\u0000\u0129\u012a\u0005*\u0000\u0000\u012aB\u0001"+
		"\u0000\u0000\u0000\u012b\u012c\u0005<\u0000\u0000\u012c\u012d\u0005<\u0000"+
		"\u0000\u012dD\u0001\u0000\u0000\u0000\u012e\u012f\u0005>\u0000\u0000\u012f"+
		"\u0130\u0005>\u0000\u0000\u0130F\u0001\u0000\u0000\u0000\u0131\u0132\u0005"+
		"p\u0000\u0000\u0132\u0133\u0005a\u0000\u0000\u0133\u0134\u0005s\u0000"+
		"\u0000\u0134\u0135\u0005s\u0000\u0000\u0135H\u0001\u0000\u0000\u0000\u0136"+
		"\u0137\u0005b\u0000\u0000\u0137\u0138\u0005r\u0000\u0000\u0138\u0139\u0005"+
		"e\u0000\u0000\u0139\u013a\u0005a\u0000\u0000\u013a\u013b\u0005k\u0000"+
		"\u0000\u013bJ\u0001\u0000\u0000\u0000\u013c\u013d\u0005c\u0000\u0000\u013d"+
		"\u013e\u0005o\u0000\u0000\u013e\u013f\u0005n\u0000\u0000\u013f\u0140\u0005"+
		"t\u0000\u0000\u0140\u0141\u0005i\u0000\u0000\u0141\u0142\u0005n\u0000"+
		"\u0000\u0142\u0143\u0005u\u0000\u0000\u0143\u0144\u0005e\u0000\u0000\u0144"+
		"L\u0001\u0000\u0000\u0000\u0145\u0146\u0005l\u0000\u0000\u0146\u0147\u0005"+
		"o\u0000\u0000\u0147\u0148\u0005g\u0000\u0000\u0148N\u0001\u0000\u0000"+
		"\u0000\u0149\u014a\u0005r\u0000\u0000\u014a\u014b\u0005e\u0000\u0000\u014b"+
		"\u014c\u0005t\u0000\u0000\u014c\u014d\u0005u\u0000\u0000\u014d\u014e\u0005"+
		"r\u0000\u0000\u014e\u014f\u0005n\u0000\u0000\u014fP\u0001\u0000\u0000"+
		"\u0000\u0150\u0151\u0005r\u0000\u0000\u0151\u0152\u0005a\u0000\u0000\u0152"+
		"\u0153\u0005i\u0000\u0000\u0153\u0154\u0005s\u0000\u0000\u0154\u0155\u0005"+
		"e\u0000\u0000\u0155R\u0001\u0000\u0000\u0000\u0156\u0157\u0005a\u0000"+
		"\u0000\u0157\u0158\u0005s\u0000\u0000\u0158\u0159\u0005s\u0000\u0000\u0159"+
		"\u015a\u0005e\u0000\u0000\u015a\u015b\u0005r\u0000\u0000\u015b\u015c\u0005"+
		"t\u0000\u0000\u015cT\u0001\u0000\u0000\u0000\u015d\u015e\u0005i\u0000"+
		"\u0000\u015e\u015f\u0005f\u0000\u0000\u015fV\u0001\u0000\u0000\u0000\u0160"+
		"\u0161\u0005e\u0000\u0000\u0161\u0162\u0005l\u0000\u0000\u0162\u0163\u0005"+
		"s\u0000\u0000\u0163\u0164\u0005e\u0000\u0000\u0164X\u0001\u0000\u0000"+
		"\u0000\u0165\u0166\u0005e\u0000\u0000\u0166\u0167\u0005l\u0000\u0000\u0167"+
		"\u0168\u0005i\u0000\u0000\u0168\u0169\u0005f\u0000\u0000\u0169Z\u0001"+
		"\u0000\u0000\u0000\u016a\u016b\u0005U\u0000\u0000\u016b\u016c\u0005N\u0000"+
		"\u0000\u016c\u016d\u0005R\u0000\u0000\u016d\u016e\u0005E\u0000\u0000\u016e"+
		"\u016f\u0005A\u0000\u0000\u016f\u0170\u0005C\u0000\u0000\u0170\u0171\u0005"+
		"H\u0000\u0000\u0171\u0172\u0005A\u0000\u0000\u0172\u0173\u0005B\u0000"+
		"\u0000\u0173\u0174\u0005L\u0000\u0000\u0174\u0175\u0005E\u0000\u0000\u0175"+
		"\\\u0001\u0000\u0000\u0000\u0176\u0177\u0005f\u0000\u0000\u0177\u0178"+
		"\u0005o\u0000\u0000\u0178\u0179\u0005r\u0000\u0000\u0179^\u0001\u0000"+
		"\u0000\u0000\u017a\u017b\u0005i\u0000\u0000\u017b\u017c\u0005n\u0000\u0000"+
		"\u017c`\u0001\u0000\u0000\u0000\u017d\u017e\u0005a\u0000\u0000\u017e\u017f"+
		"\u0005n\u0000\u0000\u017f\u0180\u0005d\u0000\u0000\u0180b\u0001\u0000"+
		"\u0000\u0000\u0181\u0182\u0005o\u0000\u0000\u0182\u0183\u0005r\u0000\u0000"+
		"\u0183d\u0001\u0000\u0000\u0000\u0184\u0185\u0005n\u0000\u0000\u0185\u0186"+
		"\u0005o\u0000\u0000\u0186\u0187\u0005t\u0000\u0000\u0187f\u0001\u0000"+
		"\u0000\u0000\u0188\u0189\u0005~\u0000\u0000\u0189h\u0001\u0000\u0000\u0000"+
		"\u018a\u018b\u0005&\u0000\u0000\u018bj\u0001\u0000\u0000\u0000\u018c\u018d"+
		"\u0005|\u0000\u0000\u018dl\u0001\u0000\u0000\u0000\u018e\u018f\u0005^"+
		"\u0000\u0000\u018fn\u0001\u0000\u0000\u0000\u0190\u0191\u0005=\u0000\u0000"+
		"\u0191\u0192\u0005=\u0000\u0000\u0192p\u0001\u0000\u0000\u0000\u0193\u0194"+
		"\u0005!\u0000\u0000\u0194\u0195\u0005=\u0000\u0000\u0195r\u0001\u0000"+
		"\u0000\u0000\u0196\u0197\u0005<\u0000\u0000\u0197\u0198\u0005=\u0000\u0000"+
		"\u0198t\u0001\u0000\u0000\u0000\u0199\u019a\u0005>\u0000\u0000\u019a\u019b"+
		"\u0005=\u0000\u0000\u019bv\u0001\u0000\u0000\u0000\u019c\u019d\u0005<"+
		"\u0000\u0000\u019dx\u0001\u0000\u0000\u0000\u019e\u019f\u0005>\u0000\u0000"+
		"\u019fz\u0001\u0000\u0000\u0000\u01a0\u01a1\u0005e\u0000\u0000\u01a1\u01a2"+
		"\u0005m\u0000\u0000\u01a2\u01a3\u0005p\u0000\u0000\u01a3\u01a4\u0005t"+
		"\u0000\u0000\u01a4\u01a5\u0005y\u0000\u0000\u01a5|\u0001\u0000\u0000\u0000"+
		"\u01a6\u01a7\u0005_\u0000\u0000\u01a7\u01a8\u0005a\u0000\u0000\u01a8\u01a9"+
		"\u0005b\u0000\u0000\u01a9\u01aa\u0005i\u0000\u0000\u01aa\u01ab\u0005_"+
		"\u0000\u0000\u01ab\u01ac\u0005d\u0000\u0000\u01ac\u01ad\u0005e\u0000\u0000"+
		"\u01ad\u01ae\u0005c\u0000\u0000\u01ae\u01af\u0005o\u0000\u0000\u01af\u01b0"+
		"\u0005d\u0000\u0000\u01b0\u01b1\u0005e\u0000\u0000\u01b1~\u0001\u0000"+
		"\u0000\u0000\u01b2\u01b3\u0005T\u0000\u0000\u01b3\u01b4\u0005r\u0000\u0000"+
		"\u01b4\u01b5\u0005u\u0000\u0000\u01b5\u01bc\u0005e\u0000\u0000\u01b6\u01b7"+
		"\u0005F\u0000\u0000\u01b7\u01b8\u0005a\u0000\u0000\u01b8\u01b9\u0005l"+
		"\u0000\u0000\u01b9\u01ba\u0005s\u0000\u0000\u01ba\u01bc\u0005e\u0000\u0000"+
		"\u01bb\u01b2\u0001\u0000\u0000\u0000\u01bb\u01b6\u0001\u0000\u0000\u0000"+
		"\u01bc\u0080\u0001\u0000\u0000\u0000\u01bd\u01c1\u0007\u0000\u0000\u0000"+
		"\u01be\u01c0\u0007\u0001\u0000\u0000\u01bf\u01be\u0001\u0000\u0000\u0000"+
		"\u01c0\u01c3\u0001\u0000\u0000\u0000\u01c1\u01bf\u0001\u0000\u0000\u0000"+
		"\u01c1\u01c2\u0001\u0000\u0000\u0000\u01c2\u0082\u0001\u0000\u0000\u0000"+
		"\u01c3\u01c1\u0001\u0000\u0000\u0000\u01c4\u01c8\u0007\u0000\u0000\u0000"+
		"\u01c5\u01c7\u0007\u0001\u0000\u0000\u01c6\u01c5\u0001\u0000\u0000\u0000"+
		"\u01c7\u01ca\u0001\u0000\u0000\u0000\u01c8\u01c6\u0001\u0000\u0000\u0000"+
		"\u01c8\u01c9\u0001\u0000\u0000\u0000\u01c9\u0084\u0001\u0000\u0000\u0000"+
		"\u01ca\u01c8\u0001\u0000\u0000\u0000\u01cb\u01cd\u0005b\u0000\u0000\u01cc"+
		"\u01cb\u0001\u0000\u0000\u0000\u01cc\u01cd\u0001\u0000\u0000\u0000\u01cd"+
		"\u01ce\u0001\u0000\u0000\u0000\u01ce\u01d3\u0005\"\u0000\u0000\u01cf\u01d2"+
		"\u0003\u0089D\u0000\u01d0\u01d2\t\u0000\u0000\u0000\u01d1\u01cf\u0001"+
		"\u0000\u0000\u0000\u01d1\u01d0\u0001\u0000\u0000\u0000\u01d2\u01d5\u0001"+
		"\u0000\u0000\u0000\u01d3\u01d4\u0001\u0000\u0000\u0000\u01d3\u01d1\u0001"+
		"\u0000\u0000\u0000\u01d4\u01d6\u0001\u0000\u0000\u0000\u01d5\u01d3\u0001"+
		"\u0000\u0000\u0000\u01d6\u01e4\u0005\"\u0000\u0000\u01d7\u01d9\u0005b"+
		"\u0000\u0000\u01d8\u01d7\u0001\u0000\u0000\u0000\u01d8\u01d9\u0001\u0000"+
		"\u0000\u0000\u01d9\u01da\u0001\u0000\u0000\u0000\u01da\u01df\u0005\'\u0000"+
		"\u0000\u01db\u01de\u0003\u0089D\u0000\u01dc\u01de\t\u0000\u0000\u0000"+
		"\u01dd\u01db\u0001\u0000\u0000\u0000\u01dd\u01dc\u0001\u0000\u0000\u0000"+
		"\u01de\u01e1\u0001\u0000\u0000\u0000\u01df\u01e0\u0001\u0000\u0000\u0000"+
		"\u01df\u01dd\u0001\u0000\u0000\u0000\u01e0\u01e2\u0001\u0000\u0000\u0000"+
		"\u01e1\u01df\u0001\u0000\u0000\u0000\u01e2\u01e4\u0005\'\u0000\u0000\u01e3"+
		"\u01cc\u0001\u0000\u0000\u0000\u01e3\u01d8\u0001\u0000\u0000\u0000\u01e4"+
		"\u0086\u0001\u0000\u0000\u0000\u01e5\u01e6\u0005\"\u0000\u0000\u01e6\u01e7"+
		"\u0005\"\u0000\u0000\u01e7\u01e8\u0005\"\u0000\u0000\u01e8\u01ed\u0001"+
		"\u0000\u0000\u0000\u01e9\u01ec\u0003\u0089D\u0000\u01ea\u01ec\t\u0000"+
		"\u0000\u0000\u01eb\u01e9\u0001\u0000\u0000\u0000\u01eb\u01ea\u0001\u0000"+
		"\u0000\u0000\u01ec\u01ef\u0001\u0000\u0000\u0000\u01ed\u01ee\u0001\u0000"+
		"\u0000\u0000\u01ed\u01eb\u0001\u0000\u0000\u0000\u01ee\u01f0\u0001\u0000"+
		"\u0000\u0000\u01ef\u01ed\u0001\u0000\u0000\u0000\u01f0\u01f1\u0005\"\u0000"+
		"\u0000\u01f1\u01f2\u0005\"\u0000\u0000\u01f2\u0202\u0005\"\u0000\u0000"+
		"\u01f3\u01f4\u0005\'\u0000\u0000\u01f4\u01f5\u0005\'\u0000\u0000\u01f5"+
		"\u01f6\u0005\'\u0000\u0000\u01f6\u01fb\u0001\u0000\u0000\u0000\u01f7\u01fa"+
		"\u0003\u0089D\u0000\u01f8\u01fa\t\u0000\u0000\u0000\u01f9\u01f7\u0001"+
		"\u0000\u0000\u0000\u01f9\u01f8\u0001\u0000\u0000\u0000\u01fa\u01fd\u0001"+
		"\u0000\u0000\u0000\u01fb\u01fc\u0001\u0000\u0000\u0000\u01fb\u01f9\u0001"+
		"\u0000\u0000\u0000\u01fc\u01fe\u0001\u0000\u0000\u0000\u01fd\u01fb\u0001"+
		"\u0000\u0000\u0000\u01fe\u01ff\u0005\'\u0000\u0000\u01ff\u0200\u0005\'"+
		"\u0000\u0000\u0200\u0202\u0005\'\u0000\u0000\u0201\u01e5\u0001\u0000\u0000"+
		"\u0000\u0201\u01f3\u0001\u0000\u0000\u0000\u0202\u0088\u0001\u0000\u0000"+
		"\u0000\u0203\u0204\u0005\\\u0000\u0000\u0204\u020a\u0005\\\u0000\u0000"+
		"\u0205\u0206\u0005\\\u0000\u0000\u0206\u020a\u0005\"\u0000\u0000\u0207"+
		"\u0208\u0005\\\u0000\u0000\u0208\u020a\u0005\'\u0000\u0000\u0209\u0203"+
		"\u0001\u0000\u0000\u0000\u0209\u0205\u0001\u0000\u0000\u0000\u0209\u0207"+
		"\u0001\u0000\u0000\u0000\u020a\u008a\u0001\u0000\u0000\u0000\u020b\u020d"+
		"\u0007\u0002\u0000\u0000\u020c\u020b\u0001\u0000\u0000\u0000\u020d\u020e"+
		"\u0001\u0000\u0000\u0000\u020e\u020c\u0001\u0000\u0000\u0000\u020e\u020f"+
		"\u0001\u0000\u0000\u0000\u020f\u008c\u0001\u0000\u0000\u0000\u0210\u0211"+
		"\u00050\u0000\u0000\u0211\u0212\u0005x\u0000\u0000\u0212\u0216\u0001\u0000"+
		"\u0000\u0000\u0213\u0215\u0007\u0003\u0000\u0000\u0214\u0213\u0001\u0000"+
		"\u0000\u0000\u0215\u0218\u0001\u0000\u0000\u0000\u0216\u0214\u0001\u0000"+
		"\u0000\u0000\u0216\u0217\u0001\u0000\u0000\u0000\u0217\u008e\u0001\u0000"+
		"\u0000\u0000\u0218\u0216\u0001\u0000\u0000\u0000\u0219\u021a\u00050\u0000"+
		"\u0000\u021a\u021b\u0005o\u0000\u0000\u021b\u021f\u0001\u0000\u0000\u0000"+
		"\u021c\u021e\u0007\u0004\u0000\u0000\u021d\u021c\u0001\u0000\u0000\u0000"+
		"\u021e\u0221\u0001\u0000\u0000\u0000\u021f\u021d\u0001\u0000\u0000\u0000"+
		"\u021f\u0220\u0001\u0000\u0000\u0000\u0220\u0090\u0001\u0000\u0000\u0000"+
		"\u0221\u021f\u0001\u0000\u0000\u0000\u0222\u0223\u00050\u0000\u0000\u0223"+
		"\u0224\u0005b\u0000\u0000\u0224\u0228\u0001\u0000\u0000\u0000\u0225\u0227"+
		"\u0007\u0005\u0000\u0000\u0226\u0225\u0001\u0000\u0000\u0000\u0227\u022a"+
		"\u0001\u0000\u0000\u0000\u0228\u0226\u0001\u0000\u0000\u0000\u0228\u0229"+
		"\u0001\u0000\u0000\u0000\u0229\u0092\u0001\u0000\u0000\u0000\u022a\u0228"+
		"\u0001\u0000\u0000\u0000\u022b\u022d\u0007\u0006\u0000\u0000\u022c\u022b"+
		"\u0001\u0000\u0000\u0000\u022c\u022d\u0001\u0000\u0000\u0000\u022d\u0235"+
		"\u0001\u0000\u0000\u0000\u022e\u0230\u0007\u0002\u0000\u0000\u022f\u022e"+
		"\u0001\u0000\u0000\u0000\u0230\u0233\u0001\u0000\u0000\u0000\u0231\u022f"+
		"\u0001\u0000\u0000\u0000\u0231\u0232\u0001\u0000\u0000\u0000\u0232\u0234"+
		"\u0001\u0000\u0000\u0000\u0233\u0231\u0001\u0000\u0000\u0000\u0234\u0236"+
		"\u0007\u0007\u0000\u0000\u0235\u0231\u0001\u0000\u0000\u0000\u0235\u0236"+
		"\u0001\u0000\u0000\u0000\u0236\u0238\u0001\u0000\u0000\u0000\u0237\u0239"+
		"\u0007\u0002\u0000\u0000\u0238\u0237\u0001\u0000\u0000\u0000\u0239\u023a"+
		"\u0001\u0000\u0000\u0000\u023a\u0238\u0001\u0000\u0000\u0000\u023a\u023b"+
		"\u0001\u0000\u0000\u0000\u023b\u0094\u0001\u0000\u0000\u0000\u023c\u023e"+
		"\u0005 \u0000\u0000\u023d\u023c\u0001\u0000\u0000\u0000\u023e\u023f\u0001"+
		"\u0000\u0000\u0000\u023f\u023d\u0001\u0000\u0000\u0000\u023f\u0240\u0001"+
		"\u0000\u0000\u0000\u0240\u0241\u0001\u0000\u0000\u0000\u0241\u0242\u0006"+
		"J\u0006\u0000\u0242\u0096\u0001\u0000\u0000\u0000\u0243\u0245\u0005\r"+
		"\u0000\u0000\u0244\u0243\u0001\u0000\u0000\u0000\u0244\u0245\u0001\u0000"+
		"\u0000\u0000\u0245\u0246\u0001\u0000\u0000\u0000\u0246\u024a\u0005\n\u0000"+
		"\u0000\u0247\u0249\u0005 \u0000\u0000\u0248\u0247\u0001\u0000\u0000\u0000"+
		"\u0249\u024c\u0001\u0000\u0000\u0000\u024a\u0248\u0001\u0000\u0000\u0000"+
		"\u024a\u024b\u0001\u0000\u0000\u0000\u024b\u024d\u0001\u0000\u0000\u0000"+
		"\u024c\u024a\u0001\u0000\u0000\u0000\u024d\u024e\u0006K\u0007\u0000\u024e"+
		"\u0098\u0001\u0000\u0000\u0000\u024f\u0253\u0005#\u0000\u0000\u0250\u0252"+
		"\b\b\u0000\u0000\u0251\u0250\u0001\u0000\u0000\u0000\u0252\u0255\u0001"+
		"\u0000\u0000\u0000\u0253\u0251\u0001\u0000\u0000\u0000\u0253\u0254\u0001"+
		"\u0000\u0000\u0000\u0254\u009a\u0001\u0000\u0000\u0000\u0255\u0253\u0001"+
		"\u0000\u0000\u0000\u001d\u0000\u01bb\u01c1\u01c8\u01cc\u01d1\u01d3\u01d8"+
		"\u01dd\u01df\u01e3\u01eb\u01ed\u01f9\u01fb\u0201\u0209\u020e\u0216\u021f"+
		"\u0228\u022c\u0231\u0235\u023a\u023f\u0244\u024a\u0253\b\u0001\b\u0000"+
		"\u0001\t\u0001\u0001\n\u0002\u0001\u000b\u0003\u0001\f\u0004\u0001\r\u0005"+
		"\u0006\u0000\u0000\u0001K\u0006";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}