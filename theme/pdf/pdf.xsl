<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:h="http://www.w3.org/1999/xhtml"
                xmlns="http://www.w3.org/1999/xhtml"
                exclude-result-prefixes="h">

  <!-- Do add border div for figure images in animal series -->
  <xsl:param name="figure.border.div" select="1"/>

  <!-- Generate separate footnote-call markers, so that we don't
       need to rely on AH counters to do footnote numbering -->
  <xsl:param name="process.footnote.callouts.only" select="1"/>

    <!-- Top-level sections listed here only; presumption is that pagenum type is set on top-level sections only,
     and is inherited by lower-level sections -->
<xsl:param name="xref.pagenum.style.for.section.by.data-type">
acknowledgments:decimal
afterword:decimal
appendix:decimal
bibliography:decimal
chapter:decimal
colophon:decimal
conclusion:decimal
copyright-page:decimal
dedication:lower-roman
foreword:lower-roman
glossary:decimal
halftitlepage:lower-roman
index:decimal
<!-- OVERRIDE BEGINS: Changing Introduction pagenum style to lower-roman to match the CSS -->
introduction:lower-roman
<!-- OVERRIDE ENDS -->
part:decimal
preface:lower-roman
titlepage:lower-roman
toc:lower-roman
</xsl:param>

<xsl:template name="string-replace-all">
  <xsl:param name="text"/>
  <xsl:param name="replace"/>
  <xsl:param name="by"/>
  <xsl:choose>
    <xsl:when test="contains($text, $replace)">
      <xsl:value-of select="substring-before($text,$replace)"/>
      <xsl:value-of select="$by"/>
      <xsl:call-template name="string-replace-all">
        <xsl:with-param name="text" select="substring-after($text,$replace)"/>
        <xsl:with-param name="replace" select="$replace"/>
        <xsl:with-param name="by" select="$by"/>
      </xsl:call-template>
    </xsl:when>
    <xsl:otherwise>
      <xsl:value-of select="$text"/>
    </xsl:otherwise>
  </xsl:choose>
</xsl:template>

<xsl:template match="h:img/@src">
  <xsl:choose>
  <xsl:when test="contains(., 'callouts/')">
    <xsl:variable name="newtext">
      <xsl:call-template name="string-replace-all">
        <xsl:with-param name="text" select="."/>
        <xsl:with-param name="replace" select="'png'"/>
        <xsl:with-param name="by" select="'pdf'"/>
      </xsl:call-template>
    </xsl:variable>
     <xsl:attribute name="src">
        <xsl:value-of select="$newtext"/>
     </xsl:attribute>
  </xsl:when>
  <xsl:otherwise>
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
   </xsl:otherwise>
  </xsl:choose>
</xsl:template>

</xsl:stylesheet>

